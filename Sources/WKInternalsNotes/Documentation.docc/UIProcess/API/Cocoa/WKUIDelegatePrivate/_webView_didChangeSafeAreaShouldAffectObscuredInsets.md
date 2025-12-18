# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didChangeSafeAreaShouldAffectObscuredInsets:)``

safe area が obscured insets に影響するかの変更を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didChangeSafeAreaShouldAffectObscuredInsets:(BOOL)safeAreaShouldAffectObscuredInsets WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKWebView の `avoidsUnsafeArea` 更新後に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L294)
- [`WKWebViewIOS.mm#L3630`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3630)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
