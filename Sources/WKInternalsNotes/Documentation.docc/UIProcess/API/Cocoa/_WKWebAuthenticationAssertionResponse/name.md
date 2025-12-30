# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/name``

ユーザー名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *name;
```

## Default Value
`WebAuthenticationAssertionResponse::name()` の値。

## Discussion
`_response->name()` を `NSString` 化して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L36)
- [`_WKWebAuthenticationAssertionResponse.mm#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
