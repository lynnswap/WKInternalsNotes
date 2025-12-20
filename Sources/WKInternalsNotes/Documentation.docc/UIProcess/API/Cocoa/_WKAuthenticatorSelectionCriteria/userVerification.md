# ``WKInternalsNotes/_WKAuthenticatorSelectionCriteria/userVerification``

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
- [`_WKAuthenticatorSelectionCriteria.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L50)
- [`_WKAuthenticatorSelectionCriteria.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L51)
- [`_WKAuthenticatorSelectionCriteria.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L31)
- [`_WKAuthenticatorSelectionCriteria.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
