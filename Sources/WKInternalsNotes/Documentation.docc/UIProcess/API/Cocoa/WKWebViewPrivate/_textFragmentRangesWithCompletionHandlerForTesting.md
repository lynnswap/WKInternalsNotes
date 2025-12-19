# ``WKInternalsNotes/WKWebView/_textFragmentRangesWithCompletionHandlerForTesting(_:)``

`_textFragmentRangesWithCompletionHandlerForTesting` を実行する。

## Objective-C Declaration
```objective-c
- (void)_textFragmentRangesWithCompletionHandlerForTesting:(void(^)(NSArray<NSValue *> *fragmentRanges))completionHandler WK_API_AVAILABLE(macos(26.0), ios(26.0), visionos(26.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L161`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L161)
- [`WKWebViewTesting.mm#L1053`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L1053)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
