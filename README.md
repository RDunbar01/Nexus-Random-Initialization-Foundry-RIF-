# Nexus Random Initialization Foundry

## [Try in your browser](<https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html>) · live browser trial

**The browser trial is live on GitHub Pages.** The exact link above was opened and its trial interface verified on 22 October 2026. This confirms page availability, not full-model execution or physical GPU qualification. The exact [single-file HTML](./Nexus_Random_Initialization_Foundry_v2_9_Browser.html) is in the repository root; GitHub's source viewer does not execute it.

Open the link and choose **Check WebGPU adapter** to inspect the interface and browser capability. The first-10-seconds goal is to reach the UI and check capability, not to download a model, finish training or guarantee inference. Load time depends on your connection and device.

**Browser trial: no Python required. Native PyTorch backend: full download required.** Download every component in [releases/2.9.1](releases/2.9.1/), not just the HTML or installer. The browser does not contain or run Python/PyTorch. See [Python and native runtime requirements](#python-and-native-runtime-requirements).

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.


> The reviewed source and installer components are published on the main branch, including the self-contained browser HTML. The browser trial linked above is published on GitHub Pages. Native Windows/Radeon qualification remains pending.

**Version 2.9.1 · published source and installer components · experimental software**

**2.9.1 native startup hotfix:** native title updates no longer starve interface timers. The browser trial remains the unchanged 2.9 edition. The previous [2.9.0 components](releases/2.9.0/) remain available for rollback; do not mix versions.

Initialize and train experimental language models from local data, inspect live progress and export supported checkpoints.

The green translucent progress dashboard and unified saveable log are retained. Save the log before closing the page. Native-only telemetry is unavailable in the browser edition.

## Reported training peak

**32,000 tokens/second peak on a Radeon RX 7900 XT** is developer-reported training throughput. It is not independently remeasured here, not a sustained-performance guarantee, and not chat-generation speed. The RX 7900 XT has a nominal 20 GB VRAM specification; available allocations depend on the runtime and other memory use. A hardware profile is not a measured benchmark score.

The desktop release is packaged with the Nexus AI-style installer: a consolidated change summary, one installation confirmation, determinate progress and reuse of compatible existing dependencies. Only verified completion should trigger app launch and installer closure; Windows launch behavior requires its own acceptance test.

## Browser capabilities and limits

Explore model initialization, local training controls and the live progress/log interface. Use supported local corpus/model inputs for actual work.

Use a compatible WebGPU browser on HTTPS or a supported secure localhost origin. The single file includes its JavaScript, CSS and WGSL kernels without a runtime CDN dependency. Browser GPU work uses the custom JavaScript/WebGPU engine, not PyTorch. Online dataset downloads, server model bridges and native hardware monitoring are unavailable; runtime network requests are blocked. External documentation links open only when selected.

A WebGPU API or adapter check is not a successful arithmetic test, a model-fit result or a performance measurement. Physical Windows 11/Radeon/WebGPU execution remains a separate qualification step.

## Desktop package and installation

The complete installer component set is in [releases/2.9.1](releases/2.9.1/). Download every file in that directory together, preserving subdirectories. Keep all numbered data parts beside [Start_Nexus.py](releases/2.9.1/Start_Nexus.py), then run `python Start_Nexus.py` with a supported Python interpreter. Read the [package guide](releases/2.9.1/README.md) before confirming installation. Each distributed data part is at most 10,000,000 bytes; the reconstructed application can be larger. Do not mix releases.

Final packaging and isolated extraction checks passed independent review. Physical Windows, WebView2 and Radeon runtime qualification remains pending; no hardware acceptance or full-model qualification is claimed.

## Python and native runtime requirements

- **Recommended launcher: standard 64-bit CPython 3.12.** The installer advertises **Python 3.11–3.14**, but the bootstrap itself does not enforce that range. Opening it on another version does not establish native compatibility.
- **This Foundry installer reuses an existing compatible PyTorch runtime only.** Select it with `--runtime`. It does not automatically install a new compute runtime. The selected Python must match its PyTorch wheels and pass the bundled native probe; the reuse path has no independent numeric Python-version gate. A passing older interpreter cannot be inferred from source alone.
- The native probe expects **PyTorch 2.14.0+rocm10.1.0**, HIP and the configured RX 7900 XT/XTX, and checks finite FP32 forward/backward results. The packaged optional dependency helper, if separately invoked, has a narrower installation gate: standard non-free-threaded x64 CPython **3.11–3.14**, Windows 11 **25H2**. Python, GPU drivers and compilers are not installed by the normal Foundry installer. See the [official AMD matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

Native Windows, WebView2, Radeon and full-model qualification remains pending. The helper’s gate and a successful runtime probe are not proof that every workload is supported.

## Measurement and validation

Native PyTorch tests distinguish synthetic scratch fixtures from loaded-model/corpus workloads. Timed training, evaluation, warm-up/compilation, prompt processing and autoregressive generation are different measurements. Report valid target tokens, elapsed time, model, context, batch size, precision, backend and hardware alongside throughput; do not count padding as useful tokens or describe a CPU result as GPU performance.

The source handoff passed recorded CPU regression and frontend checks. Browser editions passed static/DOM checks, not physical GPU arithmetic or performance qualification. A clean scoped test run does not prove absence of bugs. No maximum speed, universal model support or Windows driver certification is promised.

## Project and licensing

Developed by Rich Dunbar / Nexus Emerging Technology using AI-assisted coding and an iterative build–measure–learn process. Existing repository licenses and third-party notices remain authoritative. Model, dataset and upstream-code terms apply separately; this README grants no new reuse rights.

[Previous README, including original research citations and credits](docs/README_PREVIOUS.md). Historical release details there are not claims about this edition.

## Wiki source

[English](docs/wiki/Home.md) · [Français](docs/wiki/Home.fr.md) · [日本語](docs/wiki/Home.ja.md) · [한국어](docs/wiki/Home.ko.md). These are reviewable repository files, not a claim that the live GitHub Wiki has been published.
