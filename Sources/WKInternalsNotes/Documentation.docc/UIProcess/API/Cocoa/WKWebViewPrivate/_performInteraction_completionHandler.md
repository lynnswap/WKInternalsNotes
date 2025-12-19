# ``WKInternalsNotes/WKWebView/_performInteraction(_:completionHandler:)``

`_performInteraction` を実行する。

## Objective-C Declaration
```objective-c
- (void)_performInteraction:(_WKTextExtractionInteraction *)interaction completionHandler:(WK_SWIFT_UI_ACTOR void(^)(_WKTextExtractionInteractionResult *))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA)) NS_SWIFT_NAME(_performInteraction(_:completionHandler:));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L656`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L656)
- [`API/Cocoa/WKWebView.mm#L6748`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6748)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
