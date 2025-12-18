# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewRequestPointerLock(_:)``

ポインターロック要求を delegate に通知する（旧 API）。

## Objective-C Declaration
```objective-c
- (void)_webViewRequestPointerLock:(WKWebView *)webView WK_API_AVAILABLE(macos(10.12.4));
```

## Discussion
UIDelegate::UIClient が旧 API を検出した場合に delegate へ通知し、completion handler 付き API は別経路で処理される。

## References
- [`WKUIDelegatePrivate.h#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L154)
- [`UIDelegate.mm#L1754`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1754)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
