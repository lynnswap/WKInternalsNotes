# ``WKInternalsNotes/WKWebView/_userAgent``

`_userAgent` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_userAgent WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L217)
- [`WKWebView.mm#L4830`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4830)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
