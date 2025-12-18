# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewEndXRSession(_:withReason:)``

理由付きで XR セッション終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewEndXRSession:(WKWebView *)webView withReason:(_WKXRSessionEndReason)endReason WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
UIDelegate::UIClient が end reason を `_WKXRSessionEndReason` に変換して delegate に通知する。

## References
- [`WKUIDelegatePrivate.h#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L213)
- [`UIDelegate.mm#L2267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2267)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
