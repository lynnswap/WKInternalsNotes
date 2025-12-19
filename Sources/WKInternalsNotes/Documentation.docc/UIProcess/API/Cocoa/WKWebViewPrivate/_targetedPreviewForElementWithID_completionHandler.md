# ``WKInternalsNotes/WKWebView/_targetedPreviewForElementWithID(_:completionHandler:)``

`_targetedPreviewForElementWithID` を実行する。

## Objective-C Declaration
```objective-c
- (void)_targetedPreviewForElementWithID:(NSString *)elementID completionHandler:(WK_SWIFT_UI_ACTOR void (^)(UITargetedPreview *))completionHandler WK_API_AVAILABLE(ios(18.2), visionos(2.2));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L480`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L480)
- [`WKWebView.mm#L6344`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6344)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
