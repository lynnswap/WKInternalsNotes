# ``WKInternalsNotes/_WKWebAuthenticationPanel/getClientDataJSONWithTopOrigin(_:challenge:origin:topOrigin:crossOrigin:)``

top origin と crossOrigin の指定を含めて clientDataJSON を生成する。

## Objective-C Declaration
```objective-c
+ (NSData *)getClientDataJSONWithTopOrigin:(_WKWebAuthenticationType)type challenge:(NSData *)challenge origin:(NSString *)origin topOrigin:(NSString *)topOrigin crossOrigin:(BOOL)crossOrigin
    WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`produceClientDataJson` を `topOrigin` と `scope`（`crossOrigin` の値に応じて SameOrigin/CrossOrigin）付きで呼び出す。

## References
- [`_WKWebAuthenticationPanel.h#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L152)
- [`_WKWebAuthenticationPanel.mm#L1183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1183)
- [`_WKWebAuthenticationPanel.mm#L1187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L1187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
