# ``WKInternalsNotes/_WKWebAuthenticationPanel/type``

要求中の WebAuthn 操作種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKWebAuthenticationType type;
```

## Default Value
内部の `clientDataType` に依存する。

## Discussion
`WebAuthenticationPanel::clientDataType()` を `_WKWebAuthenticationType` に変換して返す。

## References
- [`_WKWebAuthenticationPanel.h#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L178)
- [`_WKWebAuthenticationPanel.mm#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L221)
- [`_WKWebAuthenticationPanel.mm#L249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L249)
- [`_WKWebAuthenticationPanel.mm#L251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L251)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
