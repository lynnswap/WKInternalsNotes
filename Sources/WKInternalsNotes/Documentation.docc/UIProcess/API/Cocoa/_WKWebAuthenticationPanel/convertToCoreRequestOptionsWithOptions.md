# ``WKInternalsNotes/_WKWebAuthenticationPanel/convertToCoreRequestOptionsWithOptions(_:)``

要求オプションを WebCore::PublicKeyCredentialRequestOptions に変換する。

## Objective-C Declaration
```objective-c
+ (WebCore::PublicKeyCredentialRequestOptions)convertToCoreRequestOptionsWithOptions:(_WKPublicKeyCredentialRequestOptions *)options WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、`timeout` / `relyingPartyIdentifier` / `allowCredentials` を変換して設定する。`extensionsCBOR` があれば CBOR から復元し、無い場合は `appid` を含む拡張を生成する。`userVerification` を文字列化して `userVerificationString` に保持し、`authenticatorAttachment` を変換する。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L41)
- [`_WKWebAuthenticationPanel.mm#L1095`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1095)
- [`_WKWebAuthenticationPanel.mm#L1111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1111)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
