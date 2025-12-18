# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didResignInputElementStrongPasswordAppearanceWithUserInfo:)``

強力なパスワード外観の解除を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didResignInputElementStrongPasswordAppearanceWithUserInfo:(id <NSSecureCoding>)userInfo WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
`userInfo` を `NSSecureCoding` として delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L184)
- [`UIDelegate.mm#L637`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L637)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
