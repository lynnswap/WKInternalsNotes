# ``WKInternalsNotes/WKWebView/_becomeFirstResponderWithSelectionMovingForward(_:completionHandler:)``

`_becomeFirstResponderWithSelectionMovingForward` を実行する。

## Objective-C Declaration
```objective-c
- (void)_becomeFirstResponderWithSelectionMovingForward:(BOOL)selectingForward completionHandler:(void (^)(BOOL didBecomeFirstResponder))completionHandler WK_API_AVAILABLE(ios(9_0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L771`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L771)
- [`API/ios/WKWebViewIOS.mm#L4972`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4972)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
