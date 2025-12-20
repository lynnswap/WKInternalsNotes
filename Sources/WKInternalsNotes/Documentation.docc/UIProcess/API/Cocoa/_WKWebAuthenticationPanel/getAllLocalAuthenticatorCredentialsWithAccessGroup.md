# ``WKInternalsNotes/_WKWebAuthenticationPanel/getAllLocalAuthenticatorCredentialsWithAccessGroup(_:)``

指定した access group の credential 一覧を返す。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary *> *)getAllLocalAuthenticatorCredentialsWithAccessGroup:(NSString *)accessGroup WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、指定した `accessGroup` を使って `getAllLocalAuthenticatorCredentialsImpl` を呼び出す。無効時は `nil` を返す。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L43)
- [`_WKWebAuthenticationPanel.mm#L358`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L358)
- [`_WKWebAuthenticationPanel.mm#L361`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L361)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
