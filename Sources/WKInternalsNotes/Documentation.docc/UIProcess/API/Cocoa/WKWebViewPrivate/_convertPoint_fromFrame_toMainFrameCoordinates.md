# ``WKInternalsNotes/WKWebView/_convertPoint(_:fromFrame:toMainFrameCoordinates:)``

`_convertPoint` を実行する。

## Objective-C Declaration
```objective-c
- (void)_convertPoint:(CGPoint)point fromFrame:(WKFrameInfo *)frame toMainFrameCoordinates:(void (^)(CGPoint, NSError *error))completionHandler WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L443`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L443)
- [`API/Cocoa/WKWebView.mm#L4293`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4293)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
