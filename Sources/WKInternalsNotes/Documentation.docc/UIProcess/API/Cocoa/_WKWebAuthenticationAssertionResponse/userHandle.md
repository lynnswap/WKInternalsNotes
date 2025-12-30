# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/userHandle``

ユーザーハンドルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSData *userHandle;
```

## Default Value
`WebAuthenticationAssertionResponse::userHandle()` の値。

## Discussion
`_response->userHandle()` を `NSData` に変換して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L38)
- [`_WKWebAuthenticationAssertionResponse.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
