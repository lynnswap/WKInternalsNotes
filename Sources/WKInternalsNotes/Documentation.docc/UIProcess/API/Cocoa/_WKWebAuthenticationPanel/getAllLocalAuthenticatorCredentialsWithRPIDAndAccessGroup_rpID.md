# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithRPIDAndAccessGroup(_:rpID:)``

access group と RPID を指定して credential 一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary *> *)getAllLocalAuthenticatorCredentialsWithRPIDAndAccessGroup:(NSString *)accessGroup rpID:(NSString *)rpID WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、`accessGroup` と `rpID` を使って `getAllLocalAuthenticatorCredentialsImpl` を呼び出す。無効時は `nil` を返す。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L45)
- [`_WKWebAuthenticationPanel.mm#L385`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L385)
- [`_WKWebAuthenticationPanel.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
