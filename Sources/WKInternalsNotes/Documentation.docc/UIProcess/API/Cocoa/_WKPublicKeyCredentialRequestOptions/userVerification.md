# ``WKInternalsNotes/_WKPublicKeyCredentialRequestOptions/userVerification``

ユーザー検証の要求を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKUserVerificationRequirement userVerification;
```

## Default Value
既定値は `_WKUserVerificationRequirementPreferred`。

## Discussion
`init` で `_WKUserVerificationRequirementPreferred` に初期化される。

## References
- [`_WKPublicKeyCredentialRequestOptions.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.h#L45)
- [`_WKPublicKeyCredentialRequestOptions.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.h#L46)
- [`_WKPublicKeyCredentialRequestOptions.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L31)
- [`_WKPublicKeyCredentialRequestOptions.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
