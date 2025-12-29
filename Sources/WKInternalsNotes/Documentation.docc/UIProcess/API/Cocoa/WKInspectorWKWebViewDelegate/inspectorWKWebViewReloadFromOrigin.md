# ``WKInternalsNotes/WKInspectorWKWebViewDelegate/inspectorWKWebViewReloadFromOrigin(_:)``

インスペクタの `WKInspectorWKWebView` の再読み込み（origin から）要求を通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorWKWebViewReloadFromOrigin:(WKInspectorWKWebView *)webView;
```

## Discussion
`WKInspectorWKWebView` の `reloadFromOrigin:` アクション実行時に呼ばれる。

## References
- [`WKInspectorWKWebView.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L78)
- [`WKInspectorWKWebView.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
