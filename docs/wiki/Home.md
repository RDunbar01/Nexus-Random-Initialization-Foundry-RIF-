# Nexus Random Initialization Foundry — Home

## [Try in your browser](<https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html>) · pending activation

Pages has not been activated or verified for this release. This is the planned HTTPS launch address, not a currently live trial. The repository HTML source does not execute in GitHub’s file viewer.

After publication, open the link and choose **Check WebGPU adapter**. The first-10-seconds goal is to inspect the UI and capability, not to download a model or guarantee training/inference. Loading depends on the connection and device.

**No Python is required for the HTML trial. A full download is required for the native PyTorch backend.** Keep the Python installer and every matching data part together. Python and PyTorch do not run in the HTML. WebGPU support, local inputs and model compatibility checks still apply.

## Python and native runtime requirements

- **Recommended launcher: standard 64-bit CPython 3.12.** The installer advertises **Python 3.11–3.14**, but the bootstrap itself does not enforce that range. Opening it on another version does not establish native compatibility.
- **This Foundry installer reuses an existing compatible PyTorch runtime only.** Select it with `--runtime`. It does not automatically install a new compute runtime. The selected Python must match its PyTorch wheels and pass the bundled native probe; the reuse path has no independent numeric Python-version gate. A passing older interpreter cannot be inferred from source alone.
- The native probe expects **PyTorch 2.14.0+rocm10.1.0**, HIP and the configured RX 7900 XT/XTX, and checks finite FP32 forward/backward results. The packaged optional dependency helper, if separately invoked, has a narrower installation gate: standard non-free-threaded x64 CPython **3.11–3.14**, Windows 11 **25H2**. Python, GPU drivers and compilers are not installed by the normal Foundry installer. See the [official AMD matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

Native Windows, WebView2, Radeon and full-model qualification remains pending. The helper’s gate and a successful runtime probe are not proof that every workload is supported.

**2.9.0 · English**

This is the reviewable Wiki source for the next release, not a claim that the live Wiki or browser trial is already published.

[English](Home.md) · [Français](Home.fr.md) · [日本語](Home.ja.md) · [한국어](Home.ko.md)

## Purpose

Initialize experimental models, train with local data and inspect live progress. The green translucent statistics and unified saveable log are retained. Save the log before closing the page.

## Choose an edition

### Browser edition

[HTML](../../Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](../../README.md)

Use a compatible WebGPU browser on HTTPS or a supported secure localhost origin. The single HTML file contains the custom JavaScript/WGSL engine. Import supported local files. No Python, PyTorch, native service, online dataset download or native GPU telemetry is available; runtime network requests are blocked. GitHub’s source viewer is not an executable trial.

### Installed edition

Extract the complete release ZIP and keep the installer with all data parts. Every distributed component must be smaller than 20,000,000 bytes; reconstructed files and model downloads can be larger. Follow the matching package manifest and installer summary. Native PyTorch settings and tests belong to the installed edition, not the HTML-only edition.

## Evidence and limits

CPU regression and static/DOM checks are not physical Windows/Radeon/WebGPU validation. Compare only equivalent model, corpus, context, batch, precision and backend conditions. Training/recovery, prompt processing and token generation rates are different measurements. No universal compatibility or maximum speed is guaranteed.

Developer-reported peak training throughput: **32,000 tokens/second on a Radeon RX 7900 XT**. Not independently reproduced here, not a sustained-performance guarantee and not chat-generation speed.

## Credits and licensing

Rich Dunbar / Nexus Emerging Technology, developed with AI-assisted coding. Existing licenses and third-party research, code, model and dataset terms remain in force. This page grants no additional license.

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.
