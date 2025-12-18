# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didRemoveAttachment:)``

Attachment 要素の削除を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didRemoveAttachment:(_WKAttachment *)attachment WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
Attachment の削除時に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L180)
- [`WKWebView.mm#L2105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
