# ``WKInternalsNotes/_WKInputDelegate/_webView(_:willSubmitFormValues:userObject:submissionHandler:)``

フォーム送信前に値を通知する（legacy）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView willSubmitFormValues:(NSDictionary *)values userObject:(NSObject <NSSecureCoding> *)userObject submissionHandler:(void (^)(void))submissionHandler;
```

## Discussion
`WKWebView` の `FormClient::willSubmitForm` で、`frameInfo` 付きの新 API が未実装の場合に呼ばれる。`textFieldValues` を `NSDictionary` に変換し、`submissionHandler` が呼ばれるまで送信を保留する。

## References
- [`_WKInputDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInputDelegate.h#L48)
- [`WKWebView.mm#L5834`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5834)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
