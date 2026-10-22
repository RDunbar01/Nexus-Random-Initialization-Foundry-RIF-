# Nexus Random Initialization Foundry — 홈

## [브라우저에서 체험하기](<https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html>) · 브라우저 진입 페이지 게시됨

HTTPS 브라우저 진입 페이지가 게시되었으며 초기 화면을 확인했습니다. 전체 WebGPU, Windows 또는 Radeon 작업 검증을 뜻하지는 않습니다. GitHub의 HTML 소스 보기에서는 앱이 실행되지 않습니다.

네이티브 **2.9.1** 패키지는 main에 게시되었습니다. 이번 시작 수정으로 네이티브 제목 업데이트가 UI 타이머를 독점하지 않도록 했습니다. 브라우저 체험판은 변경 없는 **2.9 에디션**입니다. 이전 릴리스는 유지되지만 구성 요소를 섞지 마세요. 패키지 검토와 압축 해제 검사는 통과했으나 실제 Windows, WebView2, Radeon 및 전체 모델 검증은 아직 완료되지 않았습니다.

링크를 열고 **Check WebGPU adapter**를 선택하세요. 처음 10초의 목표는 UI와 브라우저 기능을 확인하는 것이며, 모델 다운로드 완료나 학습·추론을 보장하는 것이 아닙니다. 로딩 시간은 연결 상태와 기기에 따라 달라집니다.

**HTML 체험판에는 Python이 필요하지 않습니다. 네이티브 PyTorch 백엔드에는 전체 다운로드가 필요합니다.** 같은 릴리스의 Python 설치 프로그램과 모든 데이터 조각을 함께 보관하세요. HTML 안에서 Python이나 PyTorch는 실행되지 않습니다. WebGPU 지원, 로컬 입력 파일 및 모델 호환성 확인은 별도로 필요합니다.

## Python 및 네이티브 실행 환경 요구 사항

- **권장 버전은 표준 64비트 CPython 3.12입니다.** 설치 프로그램은 **Python 3.11–3.14**를 안내하지만 부트스트랩이 이 범위를 강제하지는 않습니다. 다른 버전에서 열린다고 네이티브 호환성이 확인되는 것은 아닙니다.
- **Foundry 설치 프로그램은 호환되는 기존 PyTorch 런타임만 재사용합니다.** `--runtime`으로 지정하세요. 새 계산 런타임을 자동 설치하지 않습니다. 선택한 Python은 PyTorch wheel과 일치하고 포함된 네이티브 검사를 통과해야 합니다. 재사용 경로에는 별도의 숫자형 Python 버전 제한이 없으므로 소스만으로 이전 버전의 동작을 단정할 수 없습니다.
- 검사는 **PyTorch 2.14.0+rocm10.1.0**, HIP, 설정된 RX 7900 XT/XTX를 요구하며 FP32 순전파·역전파의 유한한 결과를 확인합니다. 포함된 의존성 도우미를 별도로 실행하여 새로 설치할 경우에는 free-threaded가 아닌 표준 x64 CPython **3.11–3.14** 및 Windows 11 **25H2**가 필요합니다. 일반 Foundry 설치 프로그램은 Python, GPU 드라이버, 컴파일러를 설치하지 않습니다. [AMD 공식 호환성 표](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)를 참조하세요.

실제 Windows, WebView2, Radeon 및 전체 모델 검증은 아직 완료되지 않았습니다. 도우미의 조건이나 검사 통과가 모든 작업의 지원을 입증하지는 않습니다.

**2.9.1 · 한국어**

게시된 릴리스 문서입니다. 아래 검증 범위와 제한을 확인하세요.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## 목적

실험용 모델을 초기화하고 로컬 데이터로 학습하며 진행 상황을 확인합니다. 녹색 반투명 통계 화면과 저장 가능한 통합 로그를 유지합니다. 페이지를 닫기 전에 로그를 저장하세요.

## 에디션 선택

### 브라우저 에디션

[HTML](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

HTTPS 또는 지원되는 보안 localhost 출처에서 WebGPU 호환 브라우저를 사용하세요. 단일 HTML 파일에 자체 JavaScript/WGSL 엔진이 포함됩니다. 지원되는 로컬 파일을 가져오세요. Python, PyTorch, 네이티브 서비스, 온라인 데이터셋 다운로드, 네이티브 GPU 측정 정보는 제공되지 않으며 실행 중 네트워크 요청은 차단됩니다. GitHub의 소스 보기 화면에서는 앱이 실행되지 않습니다.

### 설치형 에디션

[2.9.1 패키지](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1)의 모든 파일을 제공된 배치 그대로 함께 다운로드하세요. 번호가 있는 모든 `.nxd` 데이터 파트를 [Start_Nexus.py](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/Start_Nexus.py) 옆에 두고 지원되는 Python으로 `python Start_Nexus.py`를 실행하세요. 확인하기 전에 [해당 가이드](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/README.md)와 설치 요약을 읽으세요. 각 `.nxd` 파트는 **10,000,000바이트 이하**이며 설치 전 개별 배포 파일은 **20,000,000바이트 미만**입니다. 전체 압축 파일, 복원된 앱, 설치된 파일과 다운로드한 모델은 더 클 수 있습니다. 다른 릴리스를 섞지 마세요. 네이티브 PyTorch 설정과 테스트는 설치형 에디션에만 해당하며 HTML 단독 체험판의 기능이 아닙니다.

## 측정 결과와 한계

CPU 회귀 테스트와 정적 분석/DOM 검사는 실제 Windows/Radeon/WebGPU 하드웨어 검증이 아닙니다. 모델, 코퍼스, 문맥 길이, 배치, 정밀도, 백엔드가 같은 조건에서만 비교하세요. 학습/회복, 프롬프트 처리, 토큰 생성 처리량은 서로 다른 지표입니다. 모든 환경의 호환성이나 최대 속도를 보장하지 않습니다.

개발자가 보고한 최대 학습 처리량은 **Radeon RX 7900 XT에서 초당 32,000토큰**입니다. 여기서 독립적으로 재현한 수치가 아니며 지속적인 처리량을 보장하거나 채팅 생성 속도를 나타내지 않습니다.

## 제작 및 라이선스

Rich Dunbar / Nexus Emerging Technology가 AI 지원 코딩으로 개발했습니다. 기존 라이선스와 제3자 연구, 코드, 모델, 데이터셋의 이용 조건이 계속 적용됩니다. 이 페이지는 추가적인 이용 권한을 부여하지 않습니다.

## 현재 릴리스 라이선스

이 Nexus 릴리스는 Apache License 2.0으로 제공되지 않습니다. Nexus가 권리를 보유한 소프트웨어는 개인적이고 비상업적인 목적으로만 사용할 수 있습니다. 상업적 이용을 포함한 그 밖의 이용, 수정 또는 재배포에는 권리자의 명시적인 서면 동의가 필요합니다. 제3자 코드, 모델, 데이터 세트 및 별도로 라이선스된 구성 요소에는 각자의 라이선스와 고지가 계속 적용됩니다. 이미 부여된 권리와 법적으로 제한할 수 없는 권리는 변경되지 않습니다.

