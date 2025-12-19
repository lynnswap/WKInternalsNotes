# ``WKInternalsNotes/WKNavigationDelegatePrivate/_webView(_:contextMenuDidCreateDownload:)``

コンテキストメニューからのダウンロード作成を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView contextMenuDidCreateDownload:(WKDownload *)download WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
contextMenuDidCreateDownload で DownloadProxy をラップして delegate に渡す。

## References
- [`WKNavigationDelegatePrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationDelegatePrivate.h#L66)
- [`NavigationState.mm#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/NavigationState.mm#L202)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
