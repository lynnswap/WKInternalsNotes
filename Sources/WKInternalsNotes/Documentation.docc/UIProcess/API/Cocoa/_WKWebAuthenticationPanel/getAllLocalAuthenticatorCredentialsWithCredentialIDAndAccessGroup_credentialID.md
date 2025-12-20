# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithCredentialIDAndAccessGroup(_:credentialID:)``

access group と credentialID を指定して credential 一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary *> *)getAllLocalAuthenticatorCredentialsWithCredentialIDAndAccessGroup:(NSString *)accessGroup credentialID:(NSData *)credentialID WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、`accessGroup` と `credentialID` を使って `getAllLocalAuthenticatorCredentialsImpl` を呼び出す。無効時は `nil` を返す。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L46)
- [`_WKWebAuthenticationPanel.mm#L394`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L394)
- [`_WKWebAuthenticationPanel.mm#L397`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L397)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
