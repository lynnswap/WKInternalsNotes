# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/accessGroup``

アクセスグループを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *accessGroup;
```

## Default Value
`WebAuthenticationAssertionResponse::accessGroup()` の値。

## Discussion
`_response->accessGroup()` を `NSString` 化して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L42)
- [`_WKWebAuthenticationAssertionResponse.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
