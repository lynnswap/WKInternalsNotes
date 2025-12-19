# ``WKInternalsNotes/WKWebView/_isLayerTreeFrozenForTesting(_:)``

`_isLayerTreeFrozenForTesting` の状態を返す。

## Objective-C Declaration
```objective-c
- (void)_isLayerTreeFrozenForTesting:(void (^)(BOOL frozen))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L143)
- [`API/Cocoa/WKWebViewTesting.mm#L686`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L686)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
