# ``WKInternalsNotes/_WKWebAuthenticationPanelDelegate/panel(_:updateWebAuthenticationPanel:)``

WebAuthn パネルの状態更新を通知する。

## Objective-C Declaration
```objective-c
- (void)panel:(_WKWebAuthenticationPanel *)panel updateWebAuthenticationPanel:(_WKWebAuthenticationPanelUpdate)update WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
`WebAuthenticationPanelClient::updatePanel` から呼ばれる。delegate が未設定または未実装の場合は呼び出されない。`WebAuthenticationStatus` を `_WKWebAuthenticationPanelUpdate` に変換して渡す。

## References
- [`_WKWebAuthenticationPanel.h#L118`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L118)
- [`WebAuthenticationPanelClient.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L97)
- [`WebAuthenticationPanelClient.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebAuthentication/Cocoa/WebAuthenticationPanelClient.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
