# ``WKInternalsNotes/_WKAuthenticatorResponse/clientDataJSON``

クライアントデータのJSONを返す。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, strong, readonly) NSData *clientDataJSON;
```

## Default Value
各初期化メソッドで渡された `clientDataJSON` を retain した値。未指定なら `nil`。

## Discussion
初期化時に `_clientDataJSON` を retain して保持し、getter で返す。

## References
- [`_WKAuthenticatorResponse.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.h#L41)
- [`_WKAuthenticatorResponse.mm#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorResponse.mm#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
