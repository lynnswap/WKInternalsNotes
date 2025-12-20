# ``WKInternalsNotes/_WKAuthenticatorSelectionCriteria/requireResidentKey``

resident key を必須とするかを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL requireResidentKey;
```

## Default Value
既定値は `NO`。

## Discussion
`init` で `NO` に初期化される。

## References
- [`_WKAuthenticatorSelectionCriteria.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L47)
- [`_WKAuthenticatorSelectionCriteria.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.h#L48)
- [`_WKAuthenticatorSelectionCriteria.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L31)
- [`_WKAuthenticatorSelectionCriteria.mm#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorSelectionCriteria.mm#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
