# ``WKInternalsNotes/_WKAuthenticatorResponse/extensions``

拡張出力オブジェクトを返す。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, strong, readonly) _WKAuthenticationExtensionsClientOutputs *extensions;
```

## Default Value
`initWithClientDataJSON:rawId:extensions:attachment:` で渡された値。未指定なら `nil`。

## Discussion
初期化時に `extensions` を保持し、getter で `RetainPtr` の中身を返す。

## References
- [`_WKAuthenticatorResponse.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.h#L43)
- [`_WKAuthenticatorResponse.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L70)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
