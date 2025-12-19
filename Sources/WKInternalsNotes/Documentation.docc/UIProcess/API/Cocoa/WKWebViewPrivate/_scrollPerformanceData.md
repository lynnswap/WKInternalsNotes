# ``WKInternalsNotes/WKWebView/_scrollPerformanceData``

`_scrollPerformanceData` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray *_scrollPerformanceData WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L400`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L400)
- [`API/Cocoa/WKWebView.mm#L6037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6037)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
