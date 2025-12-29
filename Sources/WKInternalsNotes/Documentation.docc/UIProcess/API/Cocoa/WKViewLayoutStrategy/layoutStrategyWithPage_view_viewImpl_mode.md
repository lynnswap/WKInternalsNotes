# ``WKInternalsNotes/WKViewLayoutStrategy/layoutStrategyWithPage(_:view:viewImpl:mode:)``

指定した `WKLayoutMode` に応じた `WKViewLayoutStrategy` を生成する。

## Objective-C Declaration
```objective-c
+ (instancetype)layoutStrategyWithPage:(std::reference_wrapper<WebKit::WebPageProxy>)page view:(NSView *)view viewImpl:(std::reference_wrapper<WebKit::WebViewImpl>)webViewImpl mode:(WKLayoutMode)mode;
```

## Discussion
`mode` に応じてサブクラスを選択し、`updateLayout` を呼んで返す。

## References
- [`WKViewLayoutStrategy.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.mm#L50)
- [`WKViewLayoutStrategy.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKViewLayoutStrategy.h#L50)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
