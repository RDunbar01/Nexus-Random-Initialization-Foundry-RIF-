# Nexus Random Initialization Foundry — Home

## [Try in your browser](<https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html>) · published browser entry

The HTTPS browser entry is published and its initial screen has been checked. This is not full WebGPU, Windows or Radeon workload qualification. GitHub’s HTML source viewer does not execute the application.

The native **2.9.1** package is published on main. This startup hotfix prevents native title updates from starving interface timers. The browser trial remains the unchanged **2.9 edition**. Prior releases remain available; do not mix their components. Package review and extraction checks passed, but physical Windows, WebView2, Radeon and full-model qualification remain outstanding.

Open the link and choose **Check WebGPU adapter**. The first-10-seconds goal is to inspect the UI and capability, not to download a model or guarantee training/inference. Loading depends on the connection and device.

**No Python is required for the HTML trial. A full download is required for the native PyTorch backend.** Keep the Python installer and every matching data part together. Python and PyTorch do not run in the HTML. WebGPU support, local inputs and model compatibility checks still apply.

## Python and native runtime requirements

- **Recommended launcher: standard 64-bit CPython 3.12.** The installer advertises **Python 3.11–3.14**, but the bootstrap itself does not enforce that range. Opening it on another version does not establish native compatibility.
- **This Foundry installer reuses an existing compatible PyTorch runtime only.** Select it with `--runtime`. It does not automatically install a new compute runtime. The selected Python must match its PyTorch wheels and pass the bundled native probe; the reuse path has no independent numeric Python-version gate. A passing older interpreter cannot be inferred from source alone.
- The native probe expects **PyTorch 2.14.0+rocm10.1.0**, HIP and the configured RX 7900 XT/XTX, and checks finite FP32 forward/backward results. The packaged optional dependency helper, if separately invoked, has a narrower installation gate: standard non-free-threaded x64 CPython **3.11–3.14**, Windows 11 **25H2**. Python, GPU drivers and compilers are not installed by the normal Foundry installer. See the [official AMD matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

Native Windows, WebView2, Radeon and full-model qualification remains pending. The helper’s gate and a successful runtime probe are not proof that every workload is supported.

**2.9.1 · English**

Published release documentation. See the evidence and limits below.

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

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

## Credits and licensing

Rich Dunbar / Nexus Emerging Technology, developed with AI-assisted coding. Existing licenses and third-party research, code, model and dataset terms remain in force. This page grants no additional license.

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.

