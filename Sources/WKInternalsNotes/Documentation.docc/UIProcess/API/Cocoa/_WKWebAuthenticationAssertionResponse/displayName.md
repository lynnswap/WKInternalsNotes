# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/displayName``

表示名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *displayName;
```

## Default Value
`WebAuthenticationAssertionResponse::displayName()` の値。

## Discussion
`_response->displayName()` を `NSString` 化して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L37)
- [`_WKWebAuthenticationAssertionResponse.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
