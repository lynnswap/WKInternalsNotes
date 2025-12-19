# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewDidScroll(_:)``

WebView のスクロールを delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)_webViewDidScroll:(WKWebView *)webView WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
UIDelegate::UIClient の `pageDidScroll` がスクロールイベントを delegate に伝える。

## References
- [`WKUIDelegatePrivate.h#L319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L319)
- [`UIDelegate.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
