# ``WKInternalsNotes/_WKPublicKeyCredentialParameters/algorithm``

公開鍵パラメータのアルゴリズム識別子を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSNumber *algorithm;
```

## Default Value
`initWithAlgorithm:` で指定された値が設定される。

## Discussion
`initWithAlgorithm:` で `algorithm` を `self.algorithm` に設定する。`copy` 属性のため `NSNumber` をコピー保持する。

## References
- [`_WKPublicKeyCredentialParameters.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialParameters.h#L41)
- [`_WKPublicKeyCredentialParameters.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialParameters.mm#L31)
- [`_WKPublicKeyCredentialParameters.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialParameters.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
