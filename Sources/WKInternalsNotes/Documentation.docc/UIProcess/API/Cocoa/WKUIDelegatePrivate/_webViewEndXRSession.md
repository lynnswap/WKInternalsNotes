# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewEndXRSession(_:)``

XR セッション終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewEndXRSession:(WKWebView *)webView WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
UIDelegate::UIClient は `withReason` 版が未実装の場合にこのメソッドへフォールバックする。

## References
- [`WKUIDelegatePrivate.h#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L212)
- [`UIDelegate.mm#L2271`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2271)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
