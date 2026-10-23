# Nexus Random Initialization Foundry

**Version 2.9.1**

Initialize experimental language models from scratch, train them on local data and export supported checkpoints.

**[Try in your browser](https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html)** · [Download the desktop components](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

Open the trial to inspect the interface and choose **Check WebGPU adapter**. No Python installation is needed. The aim is a quick first look; loading a model or completing a workload depends on the inputs and device.

Native package 2.9.1; browser edition 2.9.

## What it does

- Model initialization and local corpus-based training controls.
- Live training statistics in a green translucent dashboard.
- A unified progress log that can be saved before closing the page.
- Separate custom WebGPU and installed PyTorch training paths.

## Engineering contribution

A local, inspectable workflow that connects model initialization, training progress and checkpoint export. It supports practical experiments with small language models without making a cloud training service a requirement.

## Why a single HTML file?

The browser edition packages its interface, JavaScript, CSS and WGSL kernels in one HTML file. This makes online trials easy to open, link to and inspect without a build step or runtime CDN. The file contains the browser engine, not model weights or the native PyTorch backend.

Use a compatible WebGPU browser over HTTPS. Runtime network requests, native hardware monitoring and local-server bridges are disabled. Actual training or evaluation requires supported inputs. The native PyTorch backend requires the full download.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## Python and native runtime requirements

- **Recommended launcher: standard 64-bit CPython 3.12.** The installer advertises **Python 3.11–3.14**, but the bootstrap itself does not enforce that range. Opening it on another version does not establish native compatibility.
- **This Foundry installer reuses an existing compatible PyTorch runtime only.** Select it with `--runtime`. It does not automatically install a new compute runtime. The selected Python must match its PyTorch wheels and pass the bundled native probe; the reuse path has no independent numeric Python-version gate. A passing older interpreter cannot be inferred from source alone.
- The native probe expects **PyTorch 2.14.0+rocm10.1.0**, HIP and the configured RX 7900 XT/XTX, and checks finite FP32 forward/backward results. The packaged optional dependency helper, if separately invoked, has a narrower installation gate: standard non-free-threaded x64 CPython **3.11–3.14**, Windows 11 **25H2**. Python, GPU drivers and compilers are not installed by the normal Foundry installer. See the [official AMD matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

Native Windows, WebView2, Radeon and full-model qualification remains pending. The helper’s gate and a successful runtime probe are not proof that every workload is supported.


## Purpose

Initialize experimental models, train with local data and inspect live progress. The green translucent statistics and unified saveable log are retained. Save the log before closing the page.

## Choose an edition

### Browser edition

[HTML](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

Use a compatible WebGPU browser on HTTPS or a supported secure localhost origin. The single HTML file contains the custom JavaScript/WGSL engine. Import supported local files. No Python, PyTorch, native service, online dataset download or native GPU telemetry is available; runtime network requests are blocked. GitHub’s source viewer is not an executable trial.

### Installed edition

Download every file in the [2.9.1 package](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1) together, retaining the supplied layout. Keep all numbered `.nxd` data parts beside [Start_Nexus.py](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/Start_Nexus.py) and run `python Start_Nexus.py` with the supported interpreter. Read the [matching guide](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/README.md) and installation summary before confirming. Each `.nxd` part is at most **10,000,000 bytes**; each individual distributed file, before installation, is smaller than **20,000,000 bytes**. The complete archive, reconstructed application, installed files and downloaded models can be larger. Do not mix releases. Native PyTorch settings and tests belong to the installed edition, not the HTML-only trial.

## Evidence and limits

CPU regression and static/DOM checks are not physical Windows/Radeon/WebGPU validation. Compare only equivalent model, corpus, context, batch, precision and backend conditions. Training/recovery, prompt processing and token generation rates are different measurements. No universal compatibility or maximum speed is guaranteed.

Developer-reported peak training throughput: **32,000 tokens/second on a Radeon RX 7900 XT**. Not independently reproduced here, not a sustained-performance guarantee and not chat-generation speed.

## Use and attribution

Rich Dunbar / Nexus Emerging Technology. Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. [license](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/LICENSE) · [evaluation permission (English)](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).
