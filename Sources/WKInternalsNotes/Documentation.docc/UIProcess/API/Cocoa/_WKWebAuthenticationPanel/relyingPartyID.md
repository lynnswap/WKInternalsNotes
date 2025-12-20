# ``WKInternalsNotes/_WKWebAuthenticationPanel/relyingPartyID``

Relying Party ID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *relyingPartyID;
```

## Default Value
内部の `WebAuthenticationPanel` が保持する rpId に依存する。

## Discussion
`API::WebAuthenticationPanel::rpId()` を `NSString` に変換して返す。

## References
- [`_WKWebAuthenticationPanel.h#L176`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L176)
- [`_WKWebAuthenticationPanel.mm#L184`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L184)
- [`_WKWebAuthenticationPanel.mm#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L186)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
