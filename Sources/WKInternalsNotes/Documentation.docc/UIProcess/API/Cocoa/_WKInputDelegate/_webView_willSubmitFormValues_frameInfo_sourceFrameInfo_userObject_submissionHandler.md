# ``WKInternalsNotes/_WKInputDelegate/_webView(_:willSubmitFormValues:frameInfo:sourceFrameInfo:userObject:submissionHandler:)``

フォーム送信前に値とフレーム情報を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willSubmitFormValues:(NSDictionary *)values frameInfo:(WKFrameInfo *)frameInfo sourceFrameInfo:(WKFrameInfo *)sourceFrameInfo userObject:(NSObject <NSSecureCoding> *)userObject submissionHandler:(void (^)(void))submissionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
`WKWebView` の `FormClient::willSubmitForm` から呼ばれる。`textFieldValues` を `NSDictionary` に変換し、`WKFrameInfo` の `frameInfo` / `sourceFrameInfo` を渡して `submissionHandler` が呼ばれるまで送信を保留する。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKWebView.mm#L5844`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5844)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
