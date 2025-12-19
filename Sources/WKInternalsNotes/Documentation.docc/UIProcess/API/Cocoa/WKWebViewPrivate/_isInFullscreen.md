# ``WKInternalsNotes/WKWebView/_isInFullscreen``

`_isInFullscreen` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _isInFullscreen WK_API_AVAILABLE(macos(10.12.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L407`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L407)
- [`API/Cocoa/WKWebView.mm#L6085`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6085)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
