# ``WKInternalsNotes/WKInspectorWKWebViewDelegate/inspectorWKWebViewDidMoveToWindow(_:)``

インスペクタの `WKInspectorWKWebView` がウィンドウ移動後に通知される。

## Objective-C Declaration
```objective-c
- (void)inspectorWKWebViewDidMoveToWindow:(WKInspectorWKWebView *)webView;
```

## Discussion
`WKInspectorWKWebView` の `viewDidMoveToWindow` で呼ばれる。

## References
- [`WKInspectorWKWebView.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L89)
- [`WKInspectorWKWebView.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
