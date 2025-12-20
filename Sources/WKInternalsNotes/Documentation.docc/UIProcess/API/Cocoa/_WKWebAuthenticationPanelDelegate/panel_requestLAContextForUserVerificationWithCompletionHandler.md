# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:requestLAContextForUserVerificationWithCompletionHandler:)``

LAContext を要求してユーザー検証に利用する。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel requestLAContextForUserVerificationWithCompletionHandler:(void (^)(LAContext *context))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WebAuthenticationPanelClient::requestLAContextForUserVerification` から呼ばれる。delegate が未設定または未実装の場合は `completionHandler(nil)` を呼ぶ。実装済みの場合は `CompletionHandlerCallChecker` を使って一度だけ完了させ、`LAContext` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L122)
- [`WebAuthenticationPanelClient.mm#L259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L259)
- [`WebAuthenticationPanelClient.mm#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L272)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
