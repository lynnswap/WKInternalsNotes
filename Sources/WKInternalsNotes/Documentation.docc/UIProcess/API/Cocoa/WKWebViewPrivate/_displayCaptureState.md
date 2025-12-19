# ``WKInternalsNotes/WKWebView/_displayCaptureState``

`_displayCaptureState` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKDisplayCaptureState _displayCaptureState WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L559`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L559)
- [`WKWebView.mm#L6180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6180)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
