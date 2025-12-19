# ``WKInternalsNotes/WKWebView/_setDisplayCaptureState(_:completionHandler:)``

`_setDisplayCaptureState` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setDisplayCaptureState:(WKDisplayCaptureState)state completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L575`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L575)
- [`WKWebView.mm#L6200`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6200)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
