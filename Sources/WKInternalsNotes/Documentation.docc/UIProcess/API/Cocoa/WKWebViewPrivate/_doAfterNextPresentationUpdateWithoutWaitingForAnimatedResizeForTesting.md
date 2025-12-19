# ``WKInternalsNotes/WKWebView/_doAfterNextPresentationUpdateWithoutWaitingForAnimatedResizeForTesting(_:)``

`_doAfterNextPresentationUpdateWithoutWaitingForAnimatedResizeForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextPresentationUpdateWithoutWaitingForAnimatedResizeForTesting:(void (^)(void))updateBlock;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L72)
- [`WKWebViewTesting.mm#L340`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L340)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
