# ``WKInternalsNotes/WKInspectorWKWebViewDelegate/inspectorWKWebViewDidBecomeActive(_:)``

インスペクタの `WKInspectorWKWebView` がアクティブになったことを通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorWKWebViewDidBecomeActive:(WKInspectorWKWebView *)webView;
```

## Discussion
`WKInspectorWKWebView` が `becomeFirstResponder` した場合や、同一ウィンドウがキーになった場合に呼ばれる。

## References
- [`WKInspectorWKWebView.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L95)
- [`WKInspectorWKWebView.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.mm#L102)
- [`WKInspectorWKWebView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorWKWebView.h#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
