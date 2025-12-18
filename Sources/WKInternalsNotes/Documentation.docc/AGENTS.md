# AGENTS.md — WKInternalsNotes Swift-DocC Guidelines

このフォルダ（`Sources/WKInternalsNotes/Documentation.docc/`）以下で Swift-DocC ドキュメントを作成/更新するときの最小ルール。

## Scope
- 対象: WebKit `Source/WebKit/UIProcess/` 以下の Objective-C 層（公開/非公開 API を含む）の調査メモ。
- 解析ソース（read-only）: `References/WebKit/Source/WebKit/UIProcess/`
  - `.h`: ファイル名に `Private` が付く/付かないに関わらず全て対象（public 判定は別途行う）。
  - `.m/.mm`: オプション。`@interface` ブロックのみを解析し、原則 `WK*` / `_WK*` の extension/category に限定する。
- 対象外: glib/gtk/wpe など LGPL 系ポート向けのヘッダ/実装（パス名で除外する）。

## Language
- 説明文（本文）は日本語で記述する（必要に応じて英語併記）。
- セクション見出し・定型ラベルは英語で統一する（例: `## Default Value`, `## Discussion`, `## Details`）。
- `## Metadata` 以下のメタ情報ラベルは英語で統一する（例: `Status`, `Last updated`, `WebKit revision`, `Header (WebKit repo-relative path)`）。
- コード、識別子、ファイル名、シンボル名は原文のまま（英語）でよい。

## Layout
- DocC catalog: `Sources/WKInternalsNotes/Documentation.docc`
- DocC 上で WebKit のディレクトリ階層は再現しない（`UIProcess/...` の synthetic container は作らない）。
- ファイル配置は任意だが、現状は `UIProcess/...` 以下に置く（スクリプト側の実装が追いつくまではこの前提で運用する）。
- 以降の説明で:
  - `<Type>` は DocC 上のコンテナシンボル名（例: `WKPreferences`）
  - `<Category>` は Objective-C category 名（例: `WKPrivate`）
- Module landing page: `Sources/WKInternalsNotes/Documentation.docc/WKInternalsNotes.md`
- 入口（ナビ）を “型中心” に寄せるため、モジュール直下の `## Topics` は型の一覧を中心にする。
- Type pages（型ごとのまとめ）:
  - 先頭は次の形式にする（DocC documentation extension）。
    ```markdown
    # ``WKInternalsNotes/<Type>``
    ```
  - `## Topics` は `<Category>` でグルーピングする（例: `### WKPrivate`）。
- Member pages（型メンバー=1エントリ=1ページ）:
  - 先頭は次の形式にする（DocC documentation extension）。
    ```markdown
    # ``WKInternalsNotes/<Type>/<Symbol>``
    ```
- Global pages（トップレベル=1エントリ=1ページ）:
  - トップレベルの `@protocol` / `typedef` / `NS_ENUM(NS_OPTIONS)` / `extern` は “擬似コンテナ” `WKGlobals` 以下へ集約する。
    ```markdown
    # ``WKInternalsNotes/WKGlobals/<Symbol>``
    ```
  - H1 直下は 1 行 Summary（Abstract）のみとし、作業ステータスや日付は `## Metadata`（ページ末尾）に置く。
    ```markdown
    ## Metadata
    | Key | Value |
    | --- | ----- |
    | Status | Draft |
    | Last updated | 2025-12-16 |
    ```
  - `## Metadata` は `Scripts/ensure_entry_metadata.py` で機械的に付与できる。
  - `## Declaration` は DocC が自動生成するため、Objective-C の宣言は `## Objective-C Declaration` に置く。
- Links:
  - 目次や箇条書きのリンクは `<doc:...>` ではなくシンボルリンクを使う。
    - 例: - ``WKInternalsNotes/WKPreferences/_acceleratedDrawingEnabled``

## Symbol Graph (synthetic)
- エントリを UIKit 風の「シンボル」ページとして表示するため、合成 symbol graph を同梱する。
  - File: `Sources/WKInternalsNotes/Documentation.docc/SymbolGraphs/WKInternalsNotes.WKAPI.symbols.json`
  - Generator: `Scripts/generate_webkit_uiprocess_objc_symbol_graph.py`
- symbol graph は “ヘッダ解析結果” を一次情報として生成し、次を満たすこと:
  - `@interface <Type> (<Category>)` 内の宣言は `<Type>` のメンバーとして `memberOf` を張る。
  - トップレベル宣言は `WKGlobals` 以下に寄せる（モジュール直下に散らさない）。
  - Public ヘッダ由来のシンボルは除外する（Rule A）。
- Objective-C の宣言行を更新したら、原則として symbol graph も更新する（DocC の宣言/availability 表示に影響するため）。

## Public Filtering (Rule A)
- Public シンボルは事前に除外する（“public headers から構築した publicSet と一致するものは出さない”）。
- public headers の定義（暫定）:
  - `Source/WebKit/UIProcess/API/Cocoa/` 以下の `.h` から、`*Private.h` / `*Internal.h` / `_*.h` / `*Testing.h` を除外した集合。
- 一致判定の粒度:
  - 型: シンボル名（`WKPreferences` など）
  - メンバー: `<Type> + (property name | selector)`（例: `WKPreferences + _setWebAudioEnabled:`）

## Writing Rules
- Summary / Discussion (must be behavioral)
  - H1 直下の Summary と `## Discussion` は、識別子や内部設定名の言い換えではなく「実装/挙動で何が変わるか」を簡潔に書く。
    - 例: 機能が利用可能になる/ならない、UI の項目が表示される/されない、特定のチェックがバイパスされる/されない。
  - インターフェース（型・範囲・setter/getter）を見れば分かることだけで終わらせない（最低 1 段深い根拠/挙動まで追う）。
- Default Value definition (must be stable)
  - 原則: 対象 API の「デフォルト初期化直後」の値（例: `WKWebViewConfiguration()` 直後）
  - 例外: 遅延初期化・端末条件・プロセス分離などで変動する場合は、その条件とタイミングも併記する
  - `WKPreferences` / `WebPreferences` 系の設定は、可能なら `Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml`（`WebKit` セクション）の `defaultValue` を根拠として併記する（key 名も残す）。
- Public API relationship
  - 公開APIで同等のことができる / 公開APIへの置換が明記されている場合は、`## Details` に `- Public API: <Symbol>` を追記し、`## References` に公開ヘッダのパスも追加する。
  - `- Public API:` は「シンボルが存在する」だけでは書かず、実装まで追って “公開APIとして最終的に操作できる（同等の効果が出る）” ことを確認した場合にのみ使う。
  - 迷う場合は `- Candidate Public API: <Symbol>` を使い、断言しない。
- Do not write
  - 配布/審査など運用上の注意文（「private API なので〜」等）。
  - 時点依存の注記（例: 「現状 iOS 18/macOS 15 では対象外」など、OS の最新バージョン前提の説明）。
  - 利用例コード（必要になったときに、その項目だけ追加する）。

## Evidence (keep it traceable)
- 断言は根拠（WebKit repo 相対パスと検索キー）に基づいて行い、推測だけで書かない。
- 実装抜粋（コードブロック）は、原則 `Source/WebKit/...` 由来の数行に留める（`Source/WebCore/...` 由来の抜粋は載せない）。
- WebKit のコードを大量に貼り付けない。要約し、参照したファイルパスを必ず残す（必要なら、型/関数名・selector などの検索ヒントも本文側に追記する）。
- `## References` は原則「ファイルパス」を列挙する（必要最小限の補足は可）。
  - 例: `- \`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm\``
  - 可能なら GitHub の固定revリンク（行番号付き）にする（基準revは `WebKit.revision`）。
    - 例: `- [\`WKPreferencesPrivate.h#L123\`](https://github.com/WebKit/WebKit/blob/<rev>/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L123)`
    - 原則、リンクテキストは「ファイル名（+ 行番号）」までに短縮する（URL 側は WebKit repo 相対パスを保持する）。
