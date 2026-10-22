# Nexus Random Initialization Foundry

## Current release licensing

This Nexus release is not offered under Apache License 2.0. Nexus-owned software may be used only for personal, non-commercial purposes. Any other use, including commercial use, modification or redistribution, requires express written consent from the rights holder. Third-party code, models, datasets and separately licensed components retain their own licenses and notices. Previously granted rights and rights that cannot lawfully be restricted remain unchanged.


> Complete independently reviewed installer components and self-contained browser HTML are staged in this draft PR. This is not a published GitHub Release or live Pages deployment. Native Windows/Radeon qualification remains pending.

**Version 2.9.0 · next-release staging · experimental software**

Initialize and train experimental language models from local data, inspect live progress and export supported checkpoints.

The green translucent progress dashboard and unified saveable log are retained. Save the log before closing the page. Native-only telemetry is unavailable in the browser edition.

## Reported training peak

**32,000 tokens/second peak on a Radeon RX 7900 XT** is developer-reported training throughput. It is not independently remeasured here, not a sustained-performance guarantee, and not chat-generation speed. The RX 7900 XT has a nominal 20 GB VRAM specification; available allocations depend on the runtime and other memory use. A hardware profile is not a measured benchmark score.

The desktop release is packaged with the Nexus AI-style installer: a consolidated change summary, one installation confirmation, determinate progress and reuse of compatible existing dependencies. Only verified completion should trigger app launch and installer closure; Windows launch behavior requires its own acceptance test.

## Browser trial: staged, not yet published

[Open the single-file browser edition](./Nexus_Random_Initialization_Foundry_v2_9_Browser.html). This relative link names the bundled HTML source; GitHub's file viewer does not execute it. An instant browser-trial link will be added only after an HTTPS Pages deployment has been approved and verified. No live deployment is claimed here.

Use a compatible browser with WebGPU on HTTPS or a supported secure localhost origin. Select local inputs through the file pickers. The edition includes its JavaScript, CSS and WGSL kernels in one HTML file, with no runtime CDN dependency. Online dataset downloads, server model bridges, Python, PyTorch and native hardware monitoring are not available in this browser-only build. Runtime network requests are blocked. External documentation links are opened only when selected.

GPU API availability is not a successful arithmetic test or proof that a model fits. Physical Windows 11/Radeon/WebGPU execution remains a separate qualification step.

## Desktop package and installation

The complete installer component set is in [releases/2.9.0](releases/2.9.0/). Download every file in that directory together, preserving subdirectories. Keep all numbered data parts beside [Start_Nexus.py](releases/2.9.0/Start_Nexus.py), then run `python Start_Nexus.py` with a supported Python interpreter. Read the [package guide](releases/2.9.0/README.md) before confirming installation. Each distributed data part is at most 10,000,000 bytes; the reconstructed application can be larger. Do not mix releases.

Final packaging and isolated extraction checks passed independent review. Physical Windows, WebView2 and Radeon runtime qualification remains pending; no hardware acceptance or live deployment is claimed.

### Desktop prerequisites

The current AMD installer gate targets Windows 11 **25H2**, an existing compatible AMD driver, and standard x64 CPython **3.11–3.14**. Do not generalize this gate to every Windows 11 release. Physical Windows/WebView2/Radeon acceptance remains pending. No global drivers, compiler or PATH changes are part of this installer.

Foundry reuses an existing compatible runtime only; `--runtime` selects its path. Its private `.nexus-alpha` state remains beside the extracted package. It does not silently install a new PyTorch runtime.

## Measurement and validation

Native PyTorch tests distinguish synthetic scratch fixtures from loaded-model/corpus workloads. Timed training, evaluation, warm-up/compilation, prompt processing and autoregressive generation are different measurements. Report valid target tokens, elapsed time, model, context, batch size, precision, backend and hardware alongside throughput; do not count padding as useful tokens or describe a CPU result as GPU performance.

The source handoff passed recorded CPU regression and frontend checks. Browser editions passed static/DOM checks, not physical GPU arithmetic or performance qualification. A clean scoped test run does not prove absence of bugs. No maximum speed, universal model support or Windows driver certification is promised.

## Project and licensing

Developed by Rich Dunbar / Nexus Emerging Technology using AI-assisted coding and an iterative build–measure–learn process. Existing repository licenses and third-party notices remain authoritative. Model, dataset and upstream-code terms apply separately; this README grants no new reuse rights.

[Previous README, including original research citations and credits](docs/README_PREVIOUS.md). Historical release details there are not claims about this staged edition.

## Wiki source

[English](docs/wiki/Home.md) · [Français](docs/wiki/Home.fr.md) · [日本語](docs/wiki/Home.ja.md) · [한국어](docs/wiki/Home.ko.md). These are reviewable repository files, not a claim that the live GitHub Wiki has been published.
