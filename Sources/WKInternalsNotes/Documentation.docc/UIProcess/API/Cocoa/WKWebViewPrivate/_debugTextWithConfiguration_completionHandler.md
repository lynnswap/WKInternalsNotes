# ``WKInternalsNotes/WKWebView/_debugTextWithConfiguration(_:completionHandler:)``

`_debugTextWithConfiguration` を実行する。

## Objective-C Declaration
```objective-c
- (void)_debugTextWithConfiguration:(_WKTextExtractionConfiguration *)configuration completionHandler:(WK_SWIFT_UI_ACTOR void(^)(NSString *))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA)) NS_SWIFT_NAME(_debugText(with:completionHandler:));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L655`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L655)
- [`WKWebView.mm#L6611`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6611)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
