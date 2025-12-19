# ``WKInternalsNotes/WKWebView/_mainFrame``

`_mainFrame` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKFrameHandle *_mainFrame WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L257)
- [`API/Cocoa/WKWebView.mm#L3819`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3819)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
