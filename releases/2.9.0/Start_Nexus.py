"""Nexus split-payload installer and launcher. Keep its .nxd files alongside it."""
import argparse,ast,base64,contextlib,hashlib,io,json,os,pathlib,secrets,shutil,subprocess,sys,tempfile,time,zipfile
PARTS = '[{"name":"Nexus_payload.001.nxd","bytes":10000000,"sha256":"11bd7eee8f9c8a4ec9c5c4eb400c63e1ac3800f0cbb982423a66b430dcd1c71f"},{"name":"Nexus_payload.002.nxd","bytes":10000000,"sha256":"b211f80d3426c7f387a1332fd65a46a7c6caadd2eaf3fb1af21ef60dc1e03722"},{"name":"Nexus_payload.003.nxd","bytes":10000000,"sha256":"10a18c3bd57c91469cc2081a6108cd68055ba5a6340d624f03cf8d46fb9ee70c"},{"name":"Nexus_payload.004.nxd","bytes":10000000,"sha256":"41038ec195c437eadcd4131315b913d2855475c381b9dcab7118d735b0b00f92"},{"name":"Nexus_payload.005.nxd","bytes":4743615,"sha256":"77b7dbfcb699ee19570bae97b9e104ae270994f2d68b8ffe1dd4017d77c5ef76"}]'
PAYLOAD_SHA = '0682b9be47c6742e46277ffe4af15e6c9e77988f9c4799f91ed8323ca1a9c231'
PRODUCT = 'foundry'
NAME = 'Random Initialization Foundry'
PORT = 8768
VERSION = '2.9.0'

def data_root():return package_folder()/'.nexus-alpha'
def package_folder():return pathlib.Path(sys.executable if getattr(sys,'frozen',False) else __file__).resolve().parent
def read_payload(destination):
 digest=hashlib.sha256();parts=json.loads(PARTS)
 if not isinstance(parts,list) or not 1<=len(parts)<=64:raise RuntimeError('Invalid payload inventory')
 for i,part in enumerate(parts,1):
  name='Nexus_payload.%03d.nxd'%i
  if not isinstance(part,dict) or part.get('name')!=name or type(part.get('bytes'))is not int or not 0<part['bytes']<20_000_000 or not isinstance(part.get('sha256'),str) or len(part['sha256'])!=64 or any(c not in '0123456789abcdef' for c in part['sha256']):raise RuntimeError('Invalid payload part descriptor')
 for part in parts:
  name=part['name']
  source=package_folder()/name
  if not source.is_file() or source.stat().st_size!=part['bytes']:raise RuntimeError('Missing or incomplete '+name+'. Extract ALL files from the ZIP into the same folder and retry.')
  check=hashlib.sha256()
  with source.open('rb') as f:
   while block:=f.read(1024*1024):check.update(block);digest.update(block);destination.write(block)
  if check.hexdigest()!=part['sha256']:raise RuntimeError('Corrupt '+name+'. Extract a fresh copy of the complete ZIP.')
 if digest.hexdigest()!=PAYLOAD_SHA:raise RuntimeError('Payload checksum mismatch')
 destination.seek(0)
@contextlib.contextmanager
def extraction_lock(root,timeout=120,operation='extracting this version'):
 # unpack precedes imports/startup locks: synchronize using stdlib only.
 root.parent.mkdir(parents=True,exist_ok=True)
 lock_path=root.parent/(root.name+'.unpack.lock')
 with lock_path.open('a+b') as handle:
  if handle.tell()==0:handle.write(b'0');handle.flush()
  deadline=time.monotonic()+timeout
  while True:
   handle.seek(0)
   try:
    if os.name=='nt':
     import msvcrt
     msvcrt.locking(handle.fileno(),msvcrt.LK_NBLCK,1)
    else:
     import fcntl
     fcntl.flock(handle.fileno(),fcntl.LOCK_EX|fcntl.LOCK_NB)
    break
   except OSError:
    if time.monotonic()>=deadline:raise RuntimeError('Another Nexus launcher is '+operation+'. Wait for it to finish and retry.')
    time.sleep(.05)
  try:yield
  finally:
   handle.seek(0)
   if os.name=='nt':msvcrt.locking(handle.fileno(),msvcrt.LK_UNLCK,1)
   else:fcntl.flock(handle.fileno(),fcntl.LOCK_UN)

def validate_archive(archive):
 seen=set();total=0
 entries=archive.infolist()
 if len(entries)>10000:raise RuntimeError('Invalid packaged file count')
 for entry in entries:
  name=entry.filename;path=pathlib.PurePosixPath(name)
  clean=name[:-1] if name.endswith('/') else name
  parts=clean.split('/');key=clean.casefold()
  devices={'CON','PRN','AUX','NUL','CONIN$','CONOUT$'}|{'COM'+str(i) for i in range(1,10)}|{'LPT'+str(i) for i in range(1,10)}
  bad=not clean or any(not x or x in ('.','..') or x!=x.rstrip(' .') or x.split('.')[0].upper() in devices or any(ord(c)<32 or c in '<>:"\\|?*' for c in x) for x in parts)
  total+=entry.file_size
  if bad or path.is_absolute() or entry.file_size>250*1024*1024 or total>2*1024*1024*1024 or key in seen or ((entry.external_attr>>16)&0o170000)==0o120000:raise RuntimeError('Invalid packaged path/size')
  seen.add(key)

def unpack():
 root=data_root()/'Apps'/PRODUCT/'versions'/PAYLOAD_SHA[:16]
 with tempfile.TemporaryFile() as raw:
  read_payload(raw)
  with extraction_lock(root):
   if not (root/'.ready').is_file() or (root/'.ready').read_text()!=PAYLOAD_SHA:
    # Never extract over a working version or expose a partially extracted one.
    with tempfile.TemporaryDirectory(prefix='unpack-',dir=root.parent) as staging:
     stage=pathlib.Path(staging)/'version';stage.mkdir()
     with zipfile.ZipFile(raw) as archive:
      validate_archive(archive);archive.extractall(stage)
     (stage/'.ready').write_text(PAYLOAD_SHA)
     # Keep recovery copies outside temporary staging: cleanup must not delete
     # the previous tree if both publication and rollback fail (e.g. locked path).
     backup=root.with_name(root.name+'.'+secrets.token_hex(8)+'.previous')
     if root.exists():os.replace(root,backup)
     try:os.replace(stage,root)
     except BaseException as error:
      if backup.exists():
       try:os.replace(backup,root)
       except OSError:raise RuntimeError('Previous version preserved at '+str(backup)+'. Publication and rollback failed; close the application and restore that folder before retrying.') from error
      raise
     if backup.exists():shutil.rmtree(backup)
 return root

def replace_files(entries):
 # Stage every file before changing any installed file. Roll back ordinary
 # I/O failures, preserving the former launcher, parts and installation state.
 staged=[];committed=[]
 try:
  for target,source in entries:
   token=secrets.token_hex(8)
   temp=target.with_name(target.name+'.'+token+'.copying')
   backup=target.with_name(target.name+'.'+token+'.previous')
   staged.append((target,temp,backup))
   shutil.copyfile(source,temp)
  for target,temp,backup in staged:
   existed=target.exists()
   if existed:os.replace(target,backup)
   committed.append((target,backup,existed))
   os.replace(temp,target)
 except BaseException as error:
  failed=[]
  for target,backup,existed in reversed(committed):
   try:
    if existed:os.replace(backup,target)
    else:target.unlink(missing_ok=True)
   except OSError:failed.append(str(backup if existed else target))
  if failed:raise RuntimeError('Rollback incomplete. Other files were restored where possible. Preserve these recovery paths: '+', '.join(failed)) from error
  raise
 finally:
  for target,temp,backup in staged:temp.unlink(missing_ok=True)
 # Preserve rollback copies if rollback itself failed; delete only on success.
 for target,temp,backup in staged:backup.unlink(missing_ok=True)


def python_executable():
 if not getattr(sys,'frozen',False):return pathlib.Path(sys.executable)
 for command in (['py','-3','-c','import sys; print(sys.executable)'],['python','-c','import sys; print(sys.executable)']):
  try:
   r=subprocess.run(command,capture_output=True,text=True,timeout=15)
   path=pathlib.Path(r.stdout.strip())
   if r.returncode==0 and path.is_file():return path
  except (OSError,subprocess.TimeoutExpired):pass
 raise RuntimeError('Install 64-bit Python 3.11–3.14 (3.12 recommended). The installer does not install Python or GPU drivers.')

def launcher_source(root):
 text=(root/'installer/bootstrap_template.py').read_text()
 for marker,value in [('__EMBED_PARTS__',PARTS),('__EMBED_SHA__',PAYLOAD_SHA),('__EMBED_PRODUCT__',PRODUCT),('__EMBED_NAME__',NAME),('__EMBED_PORT__',str(PORT))]:text=text.replace(marker,value,1)
 return text

def shortcut(python,launcher,icon,name):
 if os.name!='nt':return
 # PowerShell receives UTF-16 script, never interpolated shell command text.
 def q(x):return "'"+str(x).replace("'","''")+"'"
 code="$ErrorActionPreference='Stop';$w=New-Object -ComObject WScript.Shell;$d=[Environment]::GetFolderPath('Desktop');if([string]::IsNullOrWhiteSpace($d)){throw 'Windows Desktop folder is unavailable'};[System.IO.Directory]::CreateDirectory($d)|Out-Null;$path=Join-Path $d "+q(name+'.lnk')+";$s=$w.CreateShortcut($path);$s.TargetPath="+q(python)+";$s.Arguments="+q('"'+str(launcher)+'"')+";$s.WorkingDirectory="+q(launcher.parent)+";$s.Description="+q(NAME+' · build '+PAYLOAD_SHA[:12])+";$s.IconLocation="+q(str(icon)+',0')+";$s.Save();if(!(Test-Path -LiteralPath $path)){throw 'Desktop shortcut was not saved'}"
 legacy={'foundry':'Nexus Foundry','recovery':'Nexus Compression & Recovery Studio','adapter':'Nexus Adapter Optimization Studio','benchmark':'Nexus Foundry & Recovery Benchmark'}[PRODUCT]
 # Remove only this installation's old named shortcut, after the new one saved.
 code+=";$old=Join-Path $d "+q(legacy+'.lnk')+";if(Test-Path -LiteralPath $old){$prior=$w.CreateShortcut($old);if($prior.Arguments -eq "+q('"'+str(launcher)+'"')+"){Remove-Item -LiteralPath $old}}"
 r=subprocess.run(['powershell','-NoProfile','-NonInteractive','-EncodedCommand',base64.b64encode(code.encode('utf-16-le')).decode()],capture_output=True,text=True)
 if r.returncode:raise RuntimeError('Installed, but desktop shortcut creation failed: '+r.stderr[-1000:])
 import ctypes
 ctypes.windll.shell32.SHChangeNotify(0x08000000,0,None,None)

def refresh_desktop_shortcut(root,settings):
 if os.name!='nt':return
 python=python_executable();pythonw=python.with_name('pythonw.exe')
 sys.path.insert(0,str(root));from installer.products import PRODUCTS
 shortcut(pythonw if pythonw.is_file() else python,pathlib.Path(settings['installFolder'])/'Start_Nexus.py',root/('installer/assets/nexus_'+PRODUCT+'.ico'),PRODUCTS[PRODUCT]['label'])

def validate_install_target(folder):
 destination=folder/'Start_Nexus.py'
 if destination.exists():
  # Matching Nexus branding is not enough: a Foundry/Adapter launcher may use
  # the same filename and header. Read its literal identity without executing it.
  try:
   if destination.stat().st_size>1024*1024:raise ValueError('oversized launcher')
   prior=destination.read_text(encoding='utf-8');tree=ast.parse(prior)
   products=[node.value.value for node in tree.body if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='PRODUCT' for t in node.targets) and isinstance(node.value,ast.Constant)]
   owned=any(s in prior[:300] for s in ('Nexus single-file installer and launcher','Nexus split-payload installer and launcher')) and products==[PRODUCT]
  except (OSError,ValueError,SyntaxError):owned=False
  if not owned:raise RuntimeError('An unrelated or unverified Start_Nexus.py exists in the selected folder. Choose a dedicated '+PRODUCT+' folder; the existing launcher was left untouched.')
 if any((folder/n).exists() for n in ('README.txt','README.docx')) and not destination.exists():raise RuntimeError('The selected folder has an existing README. Choose a dedicated Nexus folder.')
 return destination

def install(root,folder,console,tray,desktop=True):
 folder=pathlib.Path(folder).expanduser().resolve();folder.mkdir(parents=True,exist_ok=True)
 validate_install_target(folder)
 # Serialize the shared installation settings as well as destination files.
 with extraction_lock(data_root()/'Apps'/PRODUCT/'installation',operation='publishing installation settings'):
  with extraction_lock(folder/'.nexus-install',operation='installing into this folder'):
   return install_locked(root,folder,console,tray,desktop)

def install_locked(root,folder,console,tray,desktop=True):
 if os.name=='nt':desktop=True
 destination=validate_install_target(folder)
 state=data_root()/'Apps'/PRODUCT;state.mkdir(parents=True,exist_ok=True);python=python_executable()
 settings={'name':NAME,'app':PRODUCT,'port':PORT,'console':bool(console),'tray':True if os.name=='nt' else bool(tray),'desktop':bool(desktop),'fullscreen':True,'payloadSHA':PAYLOAD_SHA,'state':str(state),'installFolder':str(folder),'sharedRuntime':str(data_root()/'Runtimes'/('amd-rocm10.1-py'+str(sys.version_info.major)+str(sys.version_info.minor)))}
 if not settings['console'] and (not settings['tray'] or os.name!='nt'):settings['console']=True
 # Verify and stage the complete new installation before touching the old one.
 with tempfile.TemporaryDirectory(prefix='install-',dir=state) as staging:
  staging=pathlib.Path(staging);entries=[]
  for part in json.loads(PARTS):
   source=package_folder()/part['name'];target=folder/part['name']
   staged=staging/part['name'];shutil.copyfile(source,staged)
   if staged.stat().st_size!=part['bytes'] or hashlib.sha256(staged.read_bytes()).hexdigest()!=part['sha256']:raise RuntimeError('Payload copy verification failed')
   if source.resolve()!=target.resolve():entries.append((target,staged))
  staged_launcher=staging/'Start_Nexus.py';staged_launcher.write_text(launcher_source(root),encoding='utf-8')
  config=state/'installation.json';staged_config=staging/'installation.json';staged_config.write_text(json.dumps(settings,indent=2))
  entries += [(destination,staged_launcher),(folder/'README.docx',root/'installer/guides'/('README_'+PRODUCT+'.docx')),(config,staged_config)]
  replace_files(entries)
 # Remove only the old guide produced by this installer, preserving user notes.
 old=folder/'README.txt'
 if old.is_file() and old.read_text(encoding='utf-8',errors='replace')==(root/'DESKTOP_RELEASE.txt').read_text():old.unlink()
 if desktop:
  shortcut_python=python.with_name('pythonw.exe') if python.with_name('pythonw.exe').is_file() else python
  sys.path.insert(0,str(root));from installer.products import PRODUCTS
  shortcut(shortcut_python,destination,root/('installer/assets/nexus_'+PRODUCT+'.ico'),PRODUCTS[PRODUCT]['label'])
 return config

def install_dialog(root):
 sys.path.insert(0,str(root));from installer.setup_ui import show
 return show(sys.modules[__name__],root)

def startup_status(child,settings,root):
 sys.path.insert(0,str(root/'installer'))
 from startup_ui import show
 show(settings,child=child,root=root)

def process_options(python,console,windows=None):
 windows=os.name=='nt' if windows is None else windows
 python=pathlib.Path(python);flags={}
 if windows:
  if console:
   python=python.with_name('python.exe')
   if not python.is_file():raise RuntimeError('Console requested but python.exe is unavailable beside the selected interpreter')
   flags['creationflags']=getattr(subprocess,'CREATE_NEW_CONSOLE',0x10)
  else:
   windowless=python.with_name('pythonw.exe')
   if windowless.is_file():python=windowless
   else:flags['creationflags']=getattr(subprocess,'CREATE_NO_WINDOW',0x08000000)
 return python,flags

def launch(root,config):
 settings=json.loads(config.read_text());python,flags=process_options(python_executable(),False if os.name=='nt' else settings['console'])
 if os.name=='nt':
  # Use the real Python interpreter, without constructing a renamed host.
  flags['creationflags']=flags.get('creationflags',0)|getattr(subprocess,'CREATE_NO_WINDOW',0x08000000)
 child=subprocess.Popen([str(python),str(root/'installer/app_supervisor.py'),str(config)],cwd=root,**flags)
 # Both console and windowless starts use the same graphical loading window.
 try:startup_status(child,settings,root)
 except ImportError:
  if not settings['console']:raise RuntimeError('Tkinter is needed for the server status window. Re-run with --console.')
 if os.name!='nt' and settings['console']:return child.wait()
 return 0

def restore_running(settings):
 if not settings.get('state'):return False
 state=pathlib.Path(settings['state'])
 try:
  status=json.loads((state/'launcher-state.json').read_text())
  if not isinstance(status,dict) or type(status.get('updatedAt')) not in (int,float):return False
  if status.get('app')!=PRODUCT or status.get('phase') not in ('starting','online','browser-needed') or time.time()-status.get('updatedAt',0)>10:return False
  request={'id':secrets.token_hex(16)};temp=state/('restore-'+request['id']+'.tmp');temp.write_text(json.dumps(request));os.replace(temp,state/'restore-request.json')
  for _ in range(35):
   try:
    if json.loads((state/'restore-response.json').read_text())==request:return True
   except (OSError,ValueError):pass
   time.sleep(.1)
 except (OSError,ValueError):pass
 return False

def choose_port(preferred):
 import socket
 for requested in (preferred,0):
  try:
   with socket.socket() as probe:
    if os.name=='nt' and hasattr(socket,'SO_EXCLUSIVEADDRUSE'):probe.setsockopt(socket.SOL_SOCKET,socket.SO_EXCLUSIVEADDRUSE,1)
    probe.bind(('127.0.0.1',requested));return probe.getsockname()[1]
  except OSError:
   if requested==0:raise

def existing_runtime(explicit,previous):
 values=[]
 if explicit:values=[pathlib.Path(explicit).expanduser()]
 else:
  if isinstance(previous.get('runtimePython'),str) and previous['runtimePython']:values.append(pathlib.Path(previous['runtimePython']))
  local=pathlib.Path(os.environ.get('LOCALAPPDATA',pathlib.Path.home()/'.local/share'))
  base=local/'Nexus'/'Runtimes'
  values.append(base/'amd-rocm10.1-py311'/'Scripts/python.exe')
  values.extend(sorted(base.glob('amd-rocm*-py*/Scripts/python.exe')))
  values.append(python_executable())
 for value in values:
  if value.is_file():return value.resolve()
 raise RuntimeError('Existing AMD Python runtime not found. Use --runtime followed by the full path to its python.exe. No runtime was installed or changed.')

def preview_foundry_install(a):
 # No .nexus-alpha directory, configuration, shortcut or runtime is created
 # before the single Install approval. UI assets live in a temporary preview.
 with tempfile.TemporaryDirectory(prefix='nexus-foundry-preview-') as preview, tempfile.TemporaryFile() as raw:
  read_payload(raw)
  with zipfile.ZipFile(raw) as archive:validate_archive(archive);archive.extractall(preview)
  root=pathlib.Path(preview);sys.path.insert(0,str(root))
  from installer.setup_ui import show,start_owned,guard_active_install
  state=data_root()/'Apps'/PRODUCT;config=state/'installation.json'
  previous=json.loads(config.read_text()) if config.is_file() else {}
  if not isinstance(previous,dict):raise RuntimeError('Invalid private application installation record: '+str(config))
  python=existing_runtime(a.runtime,previous)
  preferred=a.port if a.port is not None else previous.get('port',PORT)
  if type(preferred)is not int or not 1024<=preferred<=65535:preferred=PORT
  port=choose_port(preferred)
  def operation(report):
   guard_active_install(sys.modules[__name__])
   installed_root=unpack();state.mkdir(parents=True,exist_ok=True)
   os.environ['NEXUS_DESKTOP_STATE_DIR']=str(state);sys.path.insert(0,str(installed_root))
   from instance_control import startup_lock,atomic_json
   with startup_lock('desktop-entry-'+PRODUCT):
    installed=install(installed_root,package_folder(),not a.windowless,True,True)
    settings={'name':NAME,'app':PRODUCT,'port':port,'console':not a.windowless,
     'tray':True,'desktop':True,'fullscreen':True,'payloadSHA':PAYLOAD_SHA,'state':str(state),
     'installFolder':str(package_folder()),'sharedRuntime':str(python.parent.parent),
     'runtimePython':str(python),'installerFormat':'nexus-studio-v1'}
    atomic_json(installed,settings);report('completed','files')
    return start_owned(sys.modules[__name__],installed_root,installed,report)
  return show(sys.modules[__name__],root,operation=operation,folder=package_folder(),plan_details='Existing PyTorch: '+str(python)+'\nSelected local port: '+str(port))

def main():
 p=argparse.ArgumentParser(description='Alpha: original bundled program, private launcher state.')
 p.add_argument('--runtime');p.add_argument('--port',type=int);p.add_argument('--install',action='store_true')
 mode=p.add_mutually_exclusive_group();mode.add_argument('--console',action='store_true');mode.add_argument('--windowless',action='store_true')
 p.add_argument('--extract-only');p.add_argument('--check',action='store_true')
 a=p.parse_args()
 if a.port is not None and not 1024<=a.port<=65535:p.error('Port must be between 1024 and 65535')
 if a.check:
  with tempfile.TemporaryFile() as raw:read_payload(raw)
  print('NEXUS RANDOM INITIALIZATION FOUNDRY PACKAGE VERIFIED: all payload sizes and SHA-256 checksums match. This does not test Windows or GPU training.')
  return 0
 if not a.extract_only and (a.install or not (data_root()/'Apps'/PRODUCT/'installation.json').is_file()):return preview_foundry_install(a)
 root=unpack()
 if a.extract_only:
  shutil.copytree(root,pathlib.Path(a.extract_only),dirs_exist_ok=True);print(a.extract_only);return 0
 state=data_root()/'Apps'/PRODUCT;state.mkdir(parents=True,exist_ok=True)
 os.environ['NEXUS_DESKTOP_STATE_DIR']=str(state)
 sys.path.insert(0,str(root));from instance_control import startup_lock
 config=state/'installation.json'
 with startup_lock('desktop-entry-'+PRODUCT):
  previous=json.loads(config.read_text()) if config.is_file() else {}
  if not isinstance(previous,dict):raise RuntimeError('Invalid private application installation record: '+str(config))
  if previous and restore_running(previous):return 0
  python=existing_runtime(a.runtime,previous)
  preferred=a.port if a.port is not None else previous.get('port',PORT)
  if type(preferred)is not int or not 1024<=preferred<=65535:preferred=PORT
  port=choose_port(preferred)
  settings={'name':NAME,'app':PRODUCT,'port':port,'console':not a.windowless,
   'tray':True,'desktop':bool(previous.get('desktop',False)) if previous.get('installerFormat')=='nexus-studio-v1' else False,'fullscreen':True,'payloadSHA':PAYLOAD_SHA,'state':str(state),
   'installFolder':str(package_folder()),'sharedRuntime':str(python.parent.parent),
   'runtimePython':str(python)}
  if previous.get('installerFormat')=='nexus-studio-v1':settings['installerFormat']='nexus-studio-v1'
  from instance_control import atomic_json
  atomic_json(config,settings)
  print('Nexus Random Initialization Foundry uses its bundled version and private state: '+str(state),flush=True)
  if port!=preferred:print('Port '+str(preferred)+' is occupied. Nexus Random Initialization Foundry will use '+str(port)+'; the existing listener is unchanged.',flush=True)
  return launch(root,config)
 return 0
if __name__=='__main__':
 try:raise SystemExit(main())
 except Exception as error:
  if os.name=='nt':
   import ctypes
   ctypes.windll.user32.MessageBoxW(None,str(error),'Nexus launcher error',0x10)
  print('Nexus error:',error,file=sys.stderr);raise SystemExit(1)
