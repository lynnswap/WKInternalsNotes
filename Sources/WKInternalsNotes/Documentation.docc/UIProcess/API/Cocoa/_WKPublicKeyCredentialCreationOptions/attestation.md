# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/attestation``

アテステーションの要求方針を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKAttestationConveyancePreference attestation;
```

## Default Value
既定値は `_WKAttestationConveyancePreferenceNone`。

## Discussion
ヘッダのコメントで既定値が `None` と明記されている。`_WKAttestationConveyancePreference` を保持する単純なプロパティ。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L64)
- [`_WKPublicKeyCredentialCreationOptions.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L65)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
