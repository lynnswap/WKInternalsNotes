# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidLosePointerLock(_:)``

ポインターロック解除を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidLosePointerLock:(WKWebView *)webView WK_API_AVAILABLE(macos(10.12.4));
```

## Discussion
UIDelegate::UIClient がポインターロック解除時に delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L157`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L157)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
