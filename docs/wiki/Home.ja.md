# Nexus Random Initialization Foundry

**Version 2.9.1**

実験用の言語モデルを一から初期化し、ローカルデータで学習させ、対応するチェックポイントをエクスポートします。

**[ブラウザーで試す](https://rdunbar01.github.io/Nexus-Random-Initialization-Foundry-RIF-/Nexus_Random_Initialization_Foundry_v2_9_Browser.html)** · [デスクトップ用コンポーネントをダウンロード](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

試用ページを開いてインターフェースを確認し、**Check WebGPU adapter** を選択してください。Python のインストールは不要です。短時間で概要を確認するための入口です。モデルの読み込みや処理の完了時間は、入力と端末によって異なります。

ネイティブパッケージ 2.9.1、ブラウザー版 2.9。

## 主な機能

- モデルの初期化とローカルコーパスによる学習制御。
- 半透明の緑色ダッシュボードに表示するリアルタイム学習統計。
- ページを閉じる前に保存できる統合進捗ログ。
- 独自 WebGPU とインストール型 PyTorch の独立した学習経路。

## 技術的な貢献

モデルの初期化、学習進捗、チェックポイントの出力をつなぐ、ローカルで確認可能なワークフローです。クラウドの学習サービスを必須にせず、小規模な言語モデルの実験を支えます。

## 単一 HTML ファイルを使う理由

ブラウザー版は、インターフェース、JavaScript、CSS、WGSL カーネルを単一の HTML ファイルにまとめています。ビルド手順や実行時の CDN を必要とせず、オンラインで開き、リンクを共有し、内容を確認しやすくするための構成です。ファイルに含まれるのはブラウザー用エンジンであり、モデルの重みやネイティブ PyTorch バックエンドではありません。

HTTPS 上で WebGPU 対応ブラウザーを使用してください。実行時のネットワーク要求、ネイティブのハードウェア監視、ローカルサーバーとのブリッジは無効です。実際の学習や評価には対応する入力が必要です。ネイティブ PyTorch バックエンドには完全版のダウンロードが必要です。

[English](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home) · [Français](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.fr) · [日本語](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/wiki/Home.ko)

## Python とネイティブ実行環境の要件

- **推奨は標準64ビット CPython 3.12 です。** 案内範囲は **Python 3.11–3.14** ですが、起動用スクリプトではこの範囲を強制しません。他のバージョンで開けてもネイティブ互換性は確認できません。
- **Foundry インストーラーは既存の互換性のある PyTorch 実行環境だけを再利用します。** `--runtime` で指定してください。新しい計算用実行環境を自動インストールすることはありません。指定した Python と PyTorch wheel が対応し、同梱のネイティブテストに成功する必要があります。再利用経路には独立した Python バージョン数値の制限はなく、コードだけから古いバージョンの動作を断定できません。
- テストには **PyTorch 2.14.0+rocm10.1.0**、HIP、設定された RX 7900 XT/XTX が必要で、FP32 順伝播・逆伝播の有限値を確認します。同梱の依存関係ヘルパーを別途実行して新規インストールする場合は、標準・非 free-threaded の x64 CPython **3.11–3.14** と Windows 11 **25H2** が必要です。通常の Foundry インストーラーは Python・GPU ドライバー・コンパイラーをインストールしません。[AMD 公式互換性表](https://rocm.docs.amd.com/en/latest/compatibility/compatibility-matrix.html)を参照してください。

実機 Windows・WebView2・Radeon およびフルモデルの検証は未完了です。ヘルパーの条件やテスト成功は、すべての処理負荷への対応を証明しません。


## 目的

実験用モデルを初期化し、ローカルデータで学習させ、進捗を確認します。緑色の半透明の統計表示と、保存できる統合ログを維持しています。ページを閉じる前にログを保存してください。

## エディションの選択

### ブラウザー版

[HTML](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/Nexus_Random_Initialization_Foundry_v2_9_Browser.html) · [README](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/README.md)

HTTPS または対応する安全な localhost オリジンで、WebGPU 対応ブラウザーを使用してください。単一 HTML に独自の JavaScript/WGSL エンジンが含まれます。対応するローカルファイルを読み込んでください。Python、PyTorch、ネイティブサービス、オンラインデータセットの取得、ネイティブ GPU テレメトリーは利用できず、実行時のネットワーク要求は遮断されます。GitHub のソース表示画面ではアプリは実行されません。

### インストール版

[2.9.1 パッケージ](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/tree/main/releases/2.9.1)のすべてのファイルを、配布時の構成を保って一緒にダウンロードしてください。番号付きのすべての `.nxd` データパーツを [Start_Nexus.py](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/Start_Nexus.py) と同じ場所に置き、対応する Python で `python Start_Nexus.py` を実行します。同意前に[対応するガイド](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/releases/2.9.1/README.md)とインストール内容の概要を確認してください。各 `.nxd` パーツは **10,000,000 バイト以下**、インストール前の配布ファイルは1個あたり **20,000,000 バイト未満**です。アーカイブ全体、復元後のアプリ、インストール済みファイル、ダウンロードするモデルはこれを超える場合があります。異なるリリースを混在させないでください。ネイティブ PyTorch の設定・テストはインストール版の機能であり、HTML 単体の試用版の機能ではありません。

## 測定結果と制限

CPU 回帰テストや静的解析・DOM テストは、実機の Windows/Radeon/WebGPU 検証ではありません。モデル、コーパス、コンテキスト、バッチ、精度、バックエンドが等しい条件で比較してください。学習・回復、プロンプト処理、トークン生成の速度は別々の指標です。すべての環境での互換性や最高速度を保証しません。

開発者が報告した学習時のピークは **Radeon RX 7900 XT で毎秒 32,000 トークン**です。ここで独立に再現した数値ではなく、持続速度の保証やチャット生成速度を示すものでもありません。

## 利用条件とクレジット

Rich Dunbar / Nexus Emerging Technology. Nexus が権利を持つものについては、個人利用および社内での商用テスト・評価が許可されます。配布、改変、本番環境への導入、その他の商用利用には、明示的な書面による同意が必要です。第三者のライセンスと既に付与された権利は変更されません。 [ライセンス](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/LICENSE) · [評価用の追加許諾（英語）](https://github.com/RDunbar01/Nexus-Random-Initialization-Foundry-RIF-/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).
