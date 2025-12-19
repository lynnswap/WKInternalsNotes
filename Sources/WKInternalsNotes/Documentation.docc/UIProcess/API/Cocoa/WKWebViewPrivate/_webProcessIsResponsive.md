# ``WKInternalsNotes/WKWebView/_webProcessIsResponsive``

`_webProcessIsResponsive` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _webProcessIsResponsive WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L354`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L354)
- [`API/Cocoa/WKWebView.mm#L4905`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4905)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
