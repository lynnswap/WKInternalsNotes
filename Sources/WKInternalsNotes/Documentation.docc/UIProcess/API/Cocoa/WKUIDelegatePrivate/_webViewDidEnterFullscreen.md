# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidEnterFullscreen(_:)``

フルスクリーン開始を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidEnterFullscreen:(WKWebView *)webView WK_API_AVAILABLE(macos(10.11), ios(8.3));
```

## Discussion
UIDelegate::UIClient がフルスクリーン開始時に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L152)
- [`UIDelegate.mm#L1598`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1598)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
