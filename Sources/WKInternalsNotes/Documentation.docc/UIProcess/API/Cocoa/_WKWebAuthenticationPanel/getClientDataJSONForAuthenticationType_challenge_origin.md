# ``WKInternalsNotes/_WKWebAuthenticationPanel/getClientDataJSONForAuthenticationType(_:challenge:origin:)``

チャレンジと origin から clientDataJSON を生成する。

## Objective-C Declaration
```objective-c
+ (NSData *)getClientDataJSONForAuthenticationType:(_WKWebAuthenticationType)type challenge:(NSData *)challenge origin:(NSString *)origin WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`produceClientDataJson` を使って `clientDataJSON` を生成し返す（`ENABLE(WEB_AUTHN)` の場合）。

## References
- [`_WKWebAuthenticationPanel.h#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L151)
- [`_WKWebAuthenticationPanel.mm#L1172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1172)
- [`_WKWebAuthenticationPanel.mm#L1177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
