# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/synchronizable``

同期可能かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL synchronizable;
```

## Default Value
`WebAuthenticationAssertionResponse::synchronizable()` の値。

## Discussion
`_response->synchronizable()` の結果を返す。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L39)
- [`_WKWebAuthenticationAssertionResponse.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L61)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
