# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewWillEnterFullscreen(_:)``

フルスクリーン開始直前を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewWillEnterFullscreen:(WKWebView *)webView WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
UIDelegate::UIClient がフルスクリーン開始前に delegate へ通知する。

## References
- [`WKUIDelegatePrivate.h#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L151)
- [`UIDelegate.mm#L1582`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1582)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
