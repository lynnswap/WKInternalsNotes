# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didInsertAttachment:withSource:)``

Attachment 要素の挿入を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didInsertAttachment:(_WKAttachment *)attachment withSource:(NSString *)source WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Discussion
Attachment を挿入したタイミングで delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L181)
- [`WKWebView.mm#L2098`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2098)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
