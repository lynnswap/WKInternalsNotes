# ``WKInternalsNotes/_WKWebAuthenticationPanel/convertToCoreCreationOptionsWithOptions(_:)``

作成オプションを WebCore::PublicKeyCredentialCreationOptions に変換する。

## Objective-C Declaration
```objective-c
+ (WebCore::PublicKeyCredentialCreationOptions)convertToCoreCreationOptionsWithOptions:(_WKPublicKeyCredentialCreationOptions *)options WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合、relying party / user / publicKeyCredentialParamaters を WebCore の構造体へ変換して設定する。`timeout` を `unsignedIntValue` で設定し、`excludeCredentials` と `authenticatorSelection` を変換する。`attestation` は列挙を文字列化して `attestationString` に保持し、`extensionsCBOR` があれば CBOR から復元し、無い場合は `appid` を含む拡張を生成する。

## References
- [`_WKWebAuthenticationPanelForTesting.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanelForTesting.h#L40)
- [`_WKWebAuthenticationPanel.mm#L994`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L994)
- [`_WKWebAuthenticationPanel.mm#L1014`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1014)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
