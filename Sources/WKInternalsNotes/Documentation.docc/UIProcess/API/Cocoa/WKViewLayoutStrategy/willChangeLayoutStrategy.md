# ``WKInternalsNotes/WKViewLayoutStrategy/willChangeLayoutStrategy()``

レイアウト戦略を切り替える前に通知する。

## Objective-C Declaration
```objective-c
- (void)willChangeLayoutStrategy;
```

## Discussion
基底実装は no-op。`WKViewDynamicSizeComputedFromMinimumDocumentSizeLayoutStrategy` は `setShouldScaleViewToFitDocument(false)` と `scaleView(1)` を実行する。

## References
- [`WKViewLayoutStrategy.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L139)
- [`WKViewLayoutStrategy.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L243)
- [`WKViewLayoutStrategy.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
