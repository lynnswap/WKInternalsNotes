# ``WKInternalsNotes/_WKPublicKeyCredentialDescriptor/identifier``

認証器の識別子を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSData *identifier;
```

## Default Value
`initWithIdentifier:` で指定された値が設定される。

## Discussion
`initWithIdentifier:` で `identifier` を `self.identifier` に設定する。`copy` 属性のためデータをコピー保持する。

## References
- [`_WKPublicKeyCredentialDescriptor.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialDescriptor.h#L41)
- [`_WKPublicKeyCredentialDescriptor.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialDescriptor.mm#L31)
- [`_WKPublicKeyCredentialDescriptor.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialDescriptor.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
