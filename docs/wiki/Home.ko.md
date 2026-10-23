# Nexus Random Initialization Foundry

**Version 2.9.1**

실험용 언어 모델을 처음부터 초기화하고 로컬 데이터로 훈련하며 지원되는 체크포인트를 내보냅니다.

**[브라우저에서 체험하기](https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html)** · [데스크톱 구성 요소 다운로드](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

체험 페이지에서 인터페이스를 살펴보고 **Check WebGPU adapter**를 선택하세요. Python을 설치할 필요가 없습니다. 빠르게 살펴보기 위한 시작점이며, 모델을 불러오거나 작업을 완료하는 시간은 입력과 기기에 따라 달라집니다.

네이티브 패키지 2.9.1, 브라우저 에디션 2.9.

## 주요 기능

- 모델 초기화와 로컬 말뭉치 기반 훈련 제어.
- 반투명 녹색 대시보드의 실시간 훈련 통계.
- 페이지를 닫기 전에 저장할 수 있는 통합 진행 로그.
- 맞춤형 WebGPU와 설치형 PyTorch의 별도 훈련 경로.

## 기술적 기여

모델 초기화, 훈련 진행 상황과 체크포인트 내보내기를 연결하는 로컬 작업 흐름입니다. 각 단계를 확인할 수 있으며 클라우드 훈련 서비스 없이 소규모 언어 모델을 실험하도록 지원합니다.

## 단일 HTML 파일을 사용하는 이유

브라우저 에디션은 인터페이스, JavaScript, CSS와 WGSL 커널을 하나의 HTML 파일에 담습니다. 빌드 과정이나 실행 시 CDN 없이 온라인 체험을 열고, 링크를 공유하고, 내용을 살펴보기 위한 구성입니다. 이 파일에는 브라우저 엔진이 들어 있으며 모델 가중치나 네이티브 PyTorch 백엔드는 포함되지 않습니다.

HTTPS에서 WebGPU 호환 브라우저를 사용하세요. 실행 중 네트워크 요청, 네이티브 하드웨어 모니터링, 로컬 서버 연결은 비활성화되어 있습니다. 실제 훈련이나 평가에는 지원되는 입력이 필요합니다. 네이티브 PyTorch 백엔드는 전체 다운로드가 필요합니다.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## Python 및 네이티브 실행 환경 요구 사항

- **권장 버전은 표준 64비트 CPython 3.12입니다.** 설치 프로그램은 **Python 3.11–3.14**를 안내하지만 부트스트랩이 이 범위를 강제하지는 않습니다. 다른 버전에서 열린다고 네이티브 호환성이 확인되는 것은 아닙니다.
- **Foundry 설치 프로그램은 호환되는 기존 PyTorch 런타임만 재사용합니다.** `--runtime`으로 지정하세요. 새 계산 런타임을 자동 설치하지 않습니다. 선택한 Python은 PyTorch wheel과 일치하고 포함된 네이티브 검사를 통과해야 합니다. 재사용 경로에는 별도의 숫자형 Python 버전 제한이 없으므로 소스만으로 이전 버전의 동작을 단정할 수 없습니다.
- 검사는 **PyTorch 2.14.0+rocm10.1.0**, HIP, 설정된 RX 7900 XT/XTX를 요구하며 FP32 순전파·역전파의 유한한 결과를 확인합니다. 포함된 의존성 도우미를 별도로 실행하여 새로 설치할 경우에는 free-threaded가 아닌 표준 x64 CPython **3.11–3.14** 및 Windows 11 **25H2**가 필요합니다. 일반 Foundry 설치 프로그램은 Python, GPU 드라이버, 컴파일러를 설치하지 않습니다. [AMD 공식 호환성 표](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)를 참조하세요.

실제 Windows, WebView2, Radeon 및 전체 모델 검증은 아직 완료되지 않았습니다. 도우미의 조건이나 검사 통과가 모든 작업의 지원을 입증하지는 않습니다.


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

## 이용 조건 및 제작

Rich Dunbar / Nexus Emerging Technology. Nexus가 권리를 보유한 자료는 개인적 이용과 내부 상업적 테스트 및 평가에 사용할 수 있습니다. 배포, 수정, 운영 환경 배포 및 그 밖의 상업적 이용에는 명시적인 서면 동의가 필요합니다. 제3자 라이선스와 이미 부여된 권리는 변경되지 않습니다. [라이선스](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/LICENSE) · [평가 추가 허가(영문)](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).
