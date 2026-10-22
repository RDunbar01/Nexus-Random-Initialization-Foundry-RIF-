# Nexus Random Initialization Foundry — Home

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
