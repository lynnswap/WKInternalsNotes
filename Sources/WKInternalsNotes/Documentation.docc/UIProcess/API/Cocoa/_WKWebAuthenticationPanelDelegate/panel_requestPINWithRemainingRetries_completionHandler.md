# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:requestPINWithRemainingRetries:completionHandler:)``

PIN 入力を要求する。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel requestPINWithRemainingRetries:(NSUInteger)retries completionHandler:(void (^)(NSString *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`WebAuthenticationPanelClient::requestPin` から呼ばれる。delegate が未設定または未実装の場合は空文字列で `completionHandler` を呼ぶ。実装済みの場合は `CompletionHandlerCallChecker` を使って一度だけ完了させ、メインスレッドで PIN 文字列を返す。

## References
- [`_WKWebAuthenticationPanel.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L119)
- [`WebAuthenticationPanelClient.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L133)
- [`WebAuthenticationPanelClient.mm#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L152)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
