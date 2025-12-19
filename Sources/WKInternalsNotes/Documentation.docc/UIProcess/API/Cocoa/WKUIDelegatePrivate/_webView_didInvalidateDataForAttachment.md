# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didInvalidateDataForAttachment:)``

Attachment のデータ無効化を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didInvalidateDataForAttachment:(_WKAttachment *)attachment WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
Attachment のデータが無効になったタイミングで delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L159)
- [`WKWebView.mm#L2097`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L2097)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
