# Nexus Random Initialization Foundry 2.9.0

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.

## Install this complete package

1. Extract the entire ZIP to one folder. Do not run from inside the ZIP.
2. Keep `Start_Nexus.py` together with every `Nexus_payload.NNN.nxd` file. Do not mix releases.
3. With standard x64 CPython 3.11–3.14, run `python Start_Nexus.py`.
4. Read the complete change summary and choose **Install** once. Progress reports real installation stages; a moving indicator alone is not completion.
5. The installer should close only after it verifies its own loaded application window. If startup fails, retain the displayed diagnostic and do not treat installation as a successful app launch.

The current AMD runtime gate targets Windows 11 **25H2** with an existing compatible driver. This is not a claim of qualification on every Windows 11 version. Desktop WebView2/Windows/Radeon acceptance is still separate from CPU/mock tests.

To review installation again for an existing extraction, run `python Start_Nexus.py --install`. Close the running Studio using its own tray before updating; do not terminate unrelated Python processes.

## Existing runtimes and files

Foundry requires an existing compatible PyTorch runtime. Use `--runtime` to select it. Private `.nexus-alpha` state stays beside this extracted package. No replacement PyTorch runtime is installed automatically.

Missing desktop dependencies are installed app-locally. The installer does not globally uninstall/reinstall packages, replace GPU drivers, install a shared compiler or change PATH. Read the matching installer plan for exact destinations and approved actions. Preserve backups and logs before updating.

Each distributed data part is at most **10,000,000 bytes**; every other individual bundled file, including HTML and README files, is below **20,000,000 bytes**. The complete reconstructed application and ZIP may be larger in aggregate. Separately downloaded models and dependencies are not bundled distribution components. Integrity checks must pass for every part before use.

`README.docx`, if included, is a preserved legacy product guide. This README describes the new installer workflow; historical guide version labels are not the current product version.

## Runtime and benchmark scope

The installed edition can expose native PyTorch settings and supported workload tests. The separate browser-only HTML edition cannot execute Python, PyTorch or the native server. Synthetic scratch-model, loaded-model training, recovery, prompt processing and autoregressive inference measurements are not interchangeable. Report the model, corpus, valid token count, context, batch, precision, backend, hardware and elapsed time with throughput.

A clean scoped regression cycle is not proof that all bugs are absent. No physical GPU speed or universal model compatibility is guaranteed by this package description.

## Credits and licenses

Rich Dunbar / Nexus Emerging Technology, developed with AI-assisted coding. Preserve all bundled license, model, dataset, research and third-party notices. This README grants no additional license.

Developer-reported peak training throughput: **32,000 tokens/second on Radeon RX 7900 XT**, not independently reproduced here, not a sustained-rate guarantee and not chat-generation speed.

Historical full-size smoke-evidence JSON is retained in the original baseline but omitted from this release package. Current qualification summaries and reproducible tests remain included. The bundled corpus is reconstructed from verified small local fragments; its original archive SHA-256 is preserved.
