# Developers

開発者向けの短いメモです。

## 合成シンボル生成（概要）
- `Scripts/generate_webkit_uiprocess_objc_symbol_graph.py`: WebKit UIProcess から合成シンボルグラフを生成
- `Scripts/generate_webkitspi_private_symbol_graph.py`: DocC エントリから合成シンボルグラフを生成
- `Scripts/update_module_landing_topics.py`: ランディングページの Topics を更新

## WebKit 参照チェックアウト
- `./Scripts/bootstrap_webkit_reference.py` で `References/WebKit` を準備
- 出力先は `WKINTERNALS_WEBKIT_CHECKOUT` で変更可能
