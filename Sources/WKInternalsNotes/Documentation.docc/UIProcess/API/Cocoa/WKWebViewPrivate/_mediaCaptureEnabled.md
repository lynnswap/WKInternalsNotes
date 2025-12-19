# ``WKInternalsNotes/WKWebView/_mediaCaptureEnabled``

`_mediaCaptureEnabled` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaCaptureEnabled:) BOOL _mediaCaptureEnabled WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMediaCaptureEnabled:`。

## References
- [`WKWebViewPrivate.h#L414`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L414)
- [`WKWebView.mm#L838`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L838)
- [`WKWebView.mm#L838`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L838)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
