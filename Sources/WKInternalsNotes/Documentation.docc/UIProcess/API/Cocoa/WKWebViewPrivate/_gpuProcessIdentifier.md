# ``WKInternalsNotes/WKWebView/_gpuProcessIdentifier``

`_gpuProcessIdentifier` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) pid_t _gpuProcessIdentifier WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L226)
- [`API/Cocoa/WKWebView.mm#L4888`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4888)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
