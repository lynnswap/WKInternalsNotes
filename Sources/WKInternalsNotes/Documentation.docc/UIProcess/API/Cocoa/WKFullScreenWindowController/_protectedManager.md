# ``WKInternalsNotes/WKFullScreenWindowController/_protectedManager()``

`WebPageProxy` の `fullScreenManager()` を `RefPtr` で返し、取得したマネージャの寿命を保持する。ページが無い場合は `nullptr` 相当を返す。

## Objective-C Declaration
```objective-c
- (RefPtr<WebKit::WebFullScreenManagerProxy>)_protectedManager;
```

## Discussion
`_page` が有効なときだけ `fullScreenManager()` を返し、無効なら空の `RefPtr` を返す。`_manager` と同じ取得経路だが、戻り値の型で寿命を延長する点が異なる。

## References
- [`WKFullScreenWindowController.mm#L925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L925)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
