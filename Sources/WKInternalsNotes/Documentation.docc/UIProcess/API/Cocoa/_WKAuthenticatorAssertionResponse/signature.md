# ``WKInternalsNotes/_WKAuthenticatorAssertionResponse/signature``

署名データを保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSData *signature;
```

## Default Value
初期化時に渡された値を保持する。

## Discussion
初期化時に `signature` を `retain` して保持する。

## References
- [`_WKAuthenticatorAssertionResponse.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.h#L36)
- [`_WKAuthenticatorAssertionResponse.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAuthenticatorAssertionResponse.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
