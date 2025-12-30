# WKInternalsNotes

[English](README.en.md)

WebKit UIProcess の Objective-C API（公開/非公開）に関する調査メモを、
DocC のドキュメント拡張と合成シンボルグラフで管理しています。

## URL
https://lynnswap.github.io/WKInternalsNotes/

## 対象範囲
- `Source/WebKit/UIProcess` 配下の Cocoa API
- 内部 API と挙動の調査メモ

## 基準リビジョン
- 参照 WebKit リビジョンは `WebKit.revision` に固定しています。
- 参照リンクはそのリビジョンに紐づきます。

## リポジトリ構成
- `Sources/WKInternalsNotes/Documentation.docc`: 本体の DocC コンテンツ
- `Scripts`: 生成・同期用のスクリプト群
- `WebKit.revision`: 参照 WebKit リビジョン
- `References/WebKit`: WebKit のローカルチェックアウト
- `Developers.md`: 開発者向けメモ（合成シンボル生成など）

## 開発者向け
- 生成/同期スクリプトの使い方は [`Developers.md`](Developers.md) を参照してください。

## 補足
- 各ページに、挙動や既定値、参照した WebKit ソースのパスを記録します。
- 内容は調査の進行に合わせて随時更新します。
- 内容は調査メモであり、正確性・完全性を保証しません（利用は自己責任でお願いします）。

## ライセンスと帰属
- WebKit に関する著作権およびライセンスは [WebKit](https://github.com/WebKit/WebKit) プロジェクトに帰属します。
