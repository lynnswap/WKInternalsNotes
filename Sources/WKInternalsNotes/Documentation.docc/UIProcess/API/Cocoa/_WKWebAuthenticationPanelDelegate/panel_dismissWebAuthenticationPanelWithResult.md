# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:dismissWebAuthenticationPanelWithResult:)``

WebAuthn パネルの終了結果を通知する。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel dismissWebAuthenticationPanelWithResult:(_WKWebAuthenticationResult)result WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`WebAuthenticationPanelClient::dismissPanel` から呼ばれる。delegate が未設定または未実装の場合は呼び出されない。`WebAuthenticationResult` を `_WKWebAuthenticationResult` に変換して渡す。

## References
- [`_WKWebAuthenticationPanel.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L126)
- [`WebAuthenticationPanelClient.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L121)
- [`WebAuthenticationPanelClient.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L130)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
