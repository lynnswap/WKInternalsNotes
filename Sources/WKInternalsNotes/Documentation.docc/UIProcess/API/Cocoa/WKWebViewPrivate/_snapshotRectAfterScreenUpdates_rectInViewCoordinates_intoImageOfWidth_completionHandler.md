# ``WKInternalsNotes/WKWebView/_snapshotRectAfterScreenUpdates(_:rectInViewCoordinates:intoImageOfWidth:completionHandler:)``

`_snapshotRectAfterScreenUpdates` を実行する。

## Objective-C Declaration
```objective-c
- (void)_snapshotRectAfterScreenUpdates:(BOOL)afterScreenUpdates rectInViewCoordinates:(CGRect)rectInViewCoordinates intoImageOfWidth:(CGFloat)imageWidth completionHandler:(void(^)(CGImageRef))completionHandler WK_API_AVAILABLE(ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L755`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L755)
- [`API/ios/WKWebViewIOS.mm#L4802`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4802)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
