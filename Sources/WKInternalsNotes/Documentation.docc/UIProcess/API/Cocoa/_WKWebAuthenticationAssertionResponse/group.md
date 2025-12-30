# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/group``

グループ名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *group;
```

## Default Value
`WebAuthenticationAssertionResponse::group()` の値。

## Discussion
`_response->group()` を `NSString` 化して返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L40)
- [`_WKWebAuthenticationAssertionResponse.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
