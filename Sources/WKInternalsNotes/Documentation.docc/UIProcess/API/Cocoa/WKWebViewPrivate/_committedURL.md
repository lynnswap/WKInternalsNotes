# ``WKInternalsNotes/WKWebView/_committedURL``

`_committedURL` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *_committedURL;
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L215`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L215)
- [`API/Cocoa/WKWebView.mm#L4817`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4817)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
