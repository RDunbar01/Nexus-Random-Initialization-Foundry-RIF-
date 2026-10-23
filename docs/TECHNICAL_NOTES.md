# Runtime and validation notes

[Back to the overview](../README.md). These notes describe the packaged runtime checks; they are not a hardware certification.

## Python and native runtime requirements

- **Recommended launcher: standard 64-bit CPython 3.12.** The installer advertises **Python 3.11–3.14**, but the bootstrap itself does not enforce that range. Opening it on another version does not establish native compatibility.
- **This Foundry installer reuses an existing compatible PyTorch runtime only.** Select it with `--runtime`. It does not automatically install a new compute runtime. The selected Python must match its PyTorch wheels and pass the bundled native probe; the reuse path has no independent numeric Python-version gate. A passing older interpreter cannot be inferred from source alone.
- The native probe expects **PyTorch 2.14.0+rocm10.1.0**, HIP and the configured RX 7900 XT/XTX, and checks finite FP32 forward/backward results. The packaged optional dependency helper, if separately invoked, has a narrower installation gate: standard non-free-threaded x64 CPython **3.11–3.14**, Windows 11 **25H2**. Python, GPU drivers and compilers are not installed by the normal Foundry installer. See the [official AMD matrix](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html).

Native Windows, WebView2, Radeon and full-model qualification remains pending. The helper’s gate and a successful runtime probe are not proof that every workload is supported.


## Measurement and validation

Native PyTorch tests distinguish synthetic scratch fixtures from loaded-model/corpus workloads. Timed training, evaluation, warm-up/compilation, prompt processing and autoregressive generation are different measurements. Report valid target tokens, elapsed time, model, context, batch size, precision, backend and hardware alongside throughput; do not count padding as useful tokens or describe a CPU result as GPU performance.

The source handoff passed recorded CPU regression and frontend checks. Browser editions passed static/DOM checks, not physical GPU arithmetic or performance qualification. A clean scoped test run does not prove absence of bugs. No maximum speed, universal model support or Windows driver certification is promised.
