# ``WKInternalsNotes/WKWebView/_textPreviewsForElementWithID(_:completionHandler:)``

`_textPreviewsForElementWithID` を実行する。

## Objective-C Declaration
```objective-c
- (void)_textPreviewsForElementWithID:(NSString *)elementID completionHandler:(WK_SWIFT_UI_ACTOR void (^)(NSArray<_WKTextPreview *> *))completionHandler WK_API_AVAILABLE(macos(15.2));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L482`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L482)
- [`WKWebView.mm#L6363`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6363)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
