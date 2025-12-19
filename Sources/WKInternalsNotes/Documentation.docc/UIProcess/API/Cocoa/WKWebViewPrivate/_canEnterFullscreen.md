# ``WKInternalsNotes/WKWebView/_canEnterFullscreen``

`_canEnterFullscreen` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL _canEnterFullscreen WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L427`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L427)
- [`WKWebView.mm#L4252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4252)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
