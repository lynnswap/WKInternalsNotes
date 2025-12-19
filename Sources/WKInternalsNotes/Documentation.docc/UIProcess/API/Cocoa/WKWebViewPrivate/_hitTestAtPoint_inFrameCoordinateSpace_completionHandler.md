# ``WKInternalsNotes/WKWebView/_hitTestAtPoint(_:inFrameCoordinateSpace:completionHandler:)``

`_hitTestAtPoint` を実行する。

## Objective-C Declaration
```objective-c
- (void)_hitTestAtPoint:(CGPoint)point inFrameCoordinateSpace:(WKFrameInfo *)frame completionHandler:(void (^)(_WKJSHandle *, NSError *))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L454`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L454)
- [`WKWebView.mm#L4319`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4319)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
