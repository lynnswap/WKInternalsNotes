# ``WKInternalsNotes/WKInspectorWKWebViewDelegate/inspectorWKWebView(_:willMoveToWindow:)``

インスペクタの `WKInspectorWKWebView` が別ウィンドウへ移動する前に通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorWKWebView:(WKInspectorWKWebView *)webView willMoveToWindow:(NSWindow *)newWindow;
```

## Discussion
`WKInspectorWKWebView` の `viewWillMoveToWindow:` で呼ばれる。

## References
- [`WKInspectorWKWebView.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L83)
- [`WKInspectorWKWebView.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
