# ``DocCKindPlayground``

DocC の kind 表示（アイコン、role heading など）を比較するための実験用ページ。

## Discussion

このドキュメント配下の `DocCKindPlayground/*` は合成 symbol graph で生成したシンボルです。SymbolKit にマップできる kind のみが「シンボルページ」としてレンダリングされます。

一方で `DocumentationNode.Kind` のうち `isSymbol == false` のもの（例: `collectionGroup`、`tutorial` など）は symbol graph だけでは表現できないため、Article / Tutorial として別ページで「できる範囲で」再現します。

## Topics

### Grouping (non-symbol)
- <doc:DocCKindPlaygroundGroupingCollectionGroup>
- <doc:DocCKindPlaygroundGroupingCollection>

### Conceptual (non-symbol)
- <doc:DocCKindPlaygroundConceptualArticle>
- <doc:DocCKindPlaygroundConceptualSampleCode>
- <doc:DocCKindPlaygroundTutorials>
