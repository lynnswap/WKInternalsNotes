# ``WKInternalsNotes/WKWebView/_resourceDirectoryURL``

`_resourceDirectoryURL` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *_resourceDirectoryURL WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L191)
- [`API/Cocoa/WKWebView.mm#L1150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1150)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
