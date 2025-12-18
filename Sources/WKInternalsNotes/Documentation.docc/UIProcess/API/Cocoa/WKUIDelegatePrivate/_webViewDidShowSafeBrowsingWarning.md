# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidShowSafeBrowsingWarning(_:)``

セーフブラウジング警告表示を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidShowSafeBrowsingWarning:(WKWebView *)webView WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
UIDelegate::UIClient が Safe Browsing 警告表示時に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L156)
- [`UIDelegate.mm#L1799`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1799)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
