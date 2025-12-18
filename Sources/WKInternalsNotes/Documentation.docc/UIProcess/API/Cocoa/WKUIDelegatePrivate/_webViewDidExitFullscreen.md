# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidExitFullscreen(_:)``

フルスクリーン終了を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidExitFullscreen:(WKWebView *)webView WK_API_AVAILABLE(macos(10.11), ios(8.3));
```

## Discussion
UIDelegate::UIClient がフルスクリーン終了時に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L153`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L153)
- [`UIDelegate.mm#L1614`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1614)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
