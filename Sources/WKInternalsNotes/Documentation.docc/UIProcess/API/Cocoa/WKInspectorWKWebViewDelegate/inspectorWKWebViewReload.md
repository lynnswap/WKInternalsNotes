# ``WKInternalsNotes/WKInspectorWKWebViewDelegate/inspectorWKWebViewReload(_:)``

インスペクタの `WKInspectorWKWebView` の再読み込み要求を通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorWKWebViewReload:(WKInspectorWKWebView *)webView;
```

## Discussion
`WKInspectorWKWebView` の `reload:` アクション実行時に呼ばれる。

## References
- [`WKInspectorWKWebView.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L73)
- [`WKInspectorWKWebView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
