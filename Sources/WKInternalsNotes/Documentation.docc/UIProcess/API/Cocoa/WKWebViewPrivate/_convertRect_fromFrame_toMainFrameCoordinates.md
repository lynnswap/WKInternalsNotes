# ``WKInternalsNotes/WKWebView/_convertRect(_:fromFrame:toMainFrameCoordinates:)``

`_convertRect` を実行する。

## Objective-C Declaration
```objective-c
- (void)_convertRect:(CGRect)rect fromFrame:(WKFrameInfo *)frame toMainFrameCoordinates:(void (^)(CGRect, NSError *error))completionHandler WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L444`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L444)
- [`WKWebView.mm#L4306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4306)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
