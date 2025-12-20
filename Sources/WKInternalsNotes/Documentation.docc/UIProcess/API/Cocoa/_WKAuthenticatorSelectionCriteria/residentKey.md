# ``WKInternalsNotes/_WKAuthenticatorSelectionCriteria/residentKey``

resident key の要件を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKResidentKeyRequirement residentKey WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
既定値は `_WKResidentKeyRequirementNotPresent`。

## Discussion
`init` で `_WKResidentKeyRequirementNotPresent` に初期化される。

## References
- [`_WKAuthenticatorSelectionCriteria.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L44)
- [`_WKAuthenticatorSelectionCriteria.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L45)
- [`_WKAuthenticatorSelectionCriteria.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L31)
- [`_WKAuthenticatorSelectionCriteria.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
