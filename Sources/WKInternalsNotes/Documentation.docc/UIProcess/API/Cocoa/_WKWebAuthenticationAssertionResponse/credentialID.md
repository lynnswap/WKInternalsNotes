# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/credentialID``

資格情報 ID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSData *credentialID;
```

## Default Value
`WebAuthenticationAssertionResponse::credentialID()` の値。

## Discussion
`_response->credentialID()` を `NSData` に変換して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L41)
- [`_WKWebAuthenticationAssertionResponse.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L71)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
