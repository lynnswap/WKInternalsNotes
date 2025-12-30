# ``WKInternalsNotes/_WKWebAuthenticationAssertionResponse/setLAContext(_:)``

`LAContext` を設定する。

## Objective-C Declaration
```objective-c
- (void)setLAContext:(LAContext *)context WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WEB_AUTHN` 有効時に `_response->setLAContext(context)` を呼ぶ。無効時は何もしない。

## References
- [`_WKWebAuthenticationAssertionResponse.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.h#L44)
- [`_WKWebAuthenticationAssertionResponse.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationAssertionResponse.mm#L83)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
