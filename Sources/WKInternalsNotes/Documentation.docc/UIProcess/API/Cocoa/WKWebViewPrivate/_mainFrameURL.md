# ``WKInternalsNotes/WKWebView/_mainFrameURL``

`_mainFrameURL` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *_mainFrameURL WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L190)
- [`API/Cocoa/WKWebView.mm#L4589`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4589)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
