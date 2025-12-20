# ``WKInternalsNotes/_WKPublicKeyCredentialRequestOptions/allowCredentials``

許可する credential の一覧を保持する。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, copy) NSArray<_WKPublicKeyCredentialDescriptor *> *allowCredentials;
```

## Default Value
未設定の場合は `nil`。

## Discussion
自動合成されたプロパティとして保持され、`copy` 属性で配列をコピーする。

## References
- [`_WKPublicKeyCredentialRequestOptions.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.h#L44)
- [`_WKPublicKeyCredentialRequestOptions.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L41)
- [`_WKPublicKeyCredentialRequestOptions.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialRequestOptions.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
