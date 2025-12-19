# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didPerformDragOperation:)``

ドラッグ操作の処理結果を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didPerformDragOperation:(BOOL)handled WK_API_AVAILABLE(macos(10.14.4));
```

## Discussion
ドラッグ操作後に `handled` を delegate に渡す。

## References
- [`WKUIDelegatePrivate.h#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L321)
- [`WKWebViewMac.mm#L1353`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1353)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
