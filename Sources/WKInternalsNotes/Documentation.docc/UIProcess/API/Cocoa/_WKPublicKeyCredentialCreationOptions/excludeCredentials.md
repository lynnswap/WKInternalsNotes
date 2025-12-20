# ``WKInternalsNotes/_WKPublicKeyCredentialCreationOptions/excludeCredentials``

登録から除外する credential の一覧を保持する。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, copy) NSArray<_WKPublicKeyCredentialDescriptor *> *excludeCredentials;
```

## Default Value
未設定の場合は `nil`。

## Discussion
自動合成されたプロパティとして保持され、`copy` 属性で配列をコピーする。

## References
- [`_WKPublicKeyCredentialCreationOptions.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.h#L61)
- [`_WKPublicKeyCredentialCreationOptions.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L45)
- [`_WKPublicKeyCredentialCreationOptions.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKPublicKeyCredentialCreationOptions.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
