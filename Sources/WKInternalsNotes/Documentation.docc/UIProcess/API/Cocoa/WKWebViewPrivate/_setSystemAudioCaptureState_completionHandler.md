# ``WKInternalsNotes/WKWebView/_setSystemAudioCaptureState(_:completionHandler:)``

`_setSystemAudioCaptureState` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setSystemAudioCaptureState:(WKSystemAudioCaptureState)state completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L588`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L588)
- [`API/Cocoa/WKWebView.mm#L6224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
