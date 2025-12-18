# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didClickAutoFillButtonWithUserInfo:)``

AutoFill ボタン押下を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didClickAutoFillButtonWithUserInfo:(id <NSSecureCoding>)userInfo WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
`userInfo` を `NSSecureCoding` として delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`UIDelegate.mm#L1167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1167)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
