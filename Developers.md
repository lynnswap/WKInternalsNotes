# Developers

開発者向けの短いメモです。

## 合成シンボル生成（概要）
- `Scripts/generate_webkit_uiprocess_objc_symbol_graph.py`: WebKit UIProcess から合成シンボルグラフを生成
- `Scripts/generate_webkitspi_private_symbol_graph.py`: DocC エントリから合成シンボルグラフを生成
- `Scripts/update_module_landing_topics.py`: ランディングページの Topics を更新

## DocC ローカルプレビュー
- `Scripts/serve_docc.py`: DocC を一時生成してローカルサーバーでプレビュー（終了時に削除）

## DocC デプロイ
- `Scripts/build_docc_site.py`: DocC を `docs/` などに静的出力（デプロイ用、既定では出力先を削除してから生成）

## WebKit 参照チェックアウト
- `./Scripts/bootstrap_webkit_reference.py` で `References/WebKit` を準備
- 出力先は `WKINTERNALS_WEBKIT_CHECKOUT` で変更可能
