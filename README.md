# Nexus Random Initialization Foundry

**Version 2.9.1**

Initialize experimental language models from scratch, train them on local data and export supported checkpoints.

**[Try in your browser](https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html)** · [Download the desktop components](releases/2.9.1/) · [Wiki](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki)

Open the trial to inspect the interface and choose **Check WebGPU adapter**. No Python installation is needed. The aim is a quick first look, not a promise that a model will load or finish a workload in seconds.

## What it does

- Model initialization and local corpus-based training controls.
- Live training statistics in a green translucent dashboard.
- A unified progress log that can be saved before closing the page.
- Separate custom WebGPU and installed PyTorch training paths.

## Engineering contribution

A local, inspectable workflow that connects model initialization, training progress and checkpoint export. It supports practical experiments with small language models without making a cloud training service a requirement.

## Reported training result

The developer reports a peak of **32,000 training tokens/second on a Radeon RX 7900 XT**. This is not chat-generation speed or a sustained-performance guarantee. The result was not independently remeasured in this documentation review; comparisons need the model, corpus, precision, batch size and sequence length.

Native release 2.9.1 fixes a title-update loop that could delay interface timers. Its standalone browser trial remains the 2.9 edition.

## Why a single HTML file?

The browser edition packages its interface, JavaScript, CSS and WGSL kernels in one HTML file. This makes online trials easy to open, share as a link and inspect without a build step or runtime CDN. The monolithic file is a distribution choice for accessible trials, not a claim that every model or native dependency fits inside it.

Use a compatible WebGPU browser over HTTPS. The trial uses the custom browser engine, not PyTorch. Runtime network requests, native hardware monitoring and local-server bridges are disabled. Supply supported local inputs for actual training or evaluation.

## Full application and Python

**The native PyTorch backend requires the full download.** Get every file in [releases/2.9.1](releases/2.9.1/), keep the numbered data parts beside [Start_Nexus.py](releases/2.9.1/Start_Nexus.py), and run `python Start_Nexus.py`. Review the installation plan before confirming. Do not mix release components.

Use standard **64-bit CPython 3.12** for the launcher. The advertised installer range is 3.11–3.14; actual native compatibility also depends on the selected Python/PyTorch runtime and its probe. Foundry reuses an existing compatible PyTorch runtime selected with `--runtime`; its normal installer does not install a new compute runtime. See the [runtime and validation notes](docs/TECHNICAL_NOTES.md) and [package guide](releases/2.9.1/README.md) for exact conditions. Python, GPU drivers and compilers are not silently replaced.

Each data part is at most 10,000,000 bytes; each individual distribution file is below 20,000,000 bytes. Reconstructed files, installed files and model weights can be larger.

## Validation

Recorded CPU regressions, frontend checks and package-integrity checks cover the published sources. Browser launch checks establish that the interface opens; they do not establish full-model correctness or physical Windows/Radeon performance. A WebGPU adapter check is only a capability check.

## Use and attribution

Developed by Rich Dunbar / Nexus Emerging Technology. Personal use and internal commercial testing and evaluation are permitted for Nexus-owned material. Distribution, modification, production deployment and other commercial use require express written consent. Third-party licenses and previously granted rights remain unchanged. See the [license](LICENSE) and [evaluation permission](COMMERCIAL_EVALUATION_PERMISSION.md).
