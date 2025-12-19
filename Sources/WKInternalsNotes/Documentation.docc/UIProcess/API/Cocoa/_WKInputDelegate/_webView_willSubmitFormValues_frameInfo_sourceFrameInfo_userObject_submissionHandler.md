# ``WKInternalsNotes/_WKInputDelegate/_webView(_:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willSubmitFormValues:(NSDictionary *)values frameInfo:(WKFrameInfo *)frameInfo sourceFrameInfo:(WKFrameInfo *)sourceFrameInfo userObject:(NSObject <NSSecureCoding> *)userObject submissionHandler:(void (^)(void))submissionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
