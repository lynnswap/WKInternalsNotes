# ``WKInternalsNotes/WKWebView/_completeTextManipulationForItems(_:completion:)``

`_completeTextManipulationForItems` を実行する。

## Objective-C Declaration
```objective-c
- (void)_completeTextManipulationForItems:(NSArray<_WKTextManipulationItem *> *)items completion:(void(^)(NSArray<NSError *> *errors))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`completion` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L262)
- [`API/Cocoa/WKWebView.mm#L4111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
