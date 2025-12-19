# ``WKInternalsNotes/WKWebView/_systemAudioCaptureState``

`_systemAudioCaptureState` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKSystemAudioCaptureState _systemAudioCaptureState WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`WKWebViewPrivate.h#L565`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L565)
- [`WKWebView.mm#L6190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6190)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
