# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithRPID(_:)``

指定した RPID で絞り込んだ credential 一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary *> *)getAllLocalAuthenticatorCredentialsWithRPID:(NSString *)rpID WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、既定の access group と `rpID` を使って `getAllLocalAuthenticatorCredentialsImpl` を呼び出す。無効時は `nil` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L135)
- [`_WKWebAuthenticationPanel.mm#L367`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L367)
- [`_WKWebAuthenticationPanel.mm#L370`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L370)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
