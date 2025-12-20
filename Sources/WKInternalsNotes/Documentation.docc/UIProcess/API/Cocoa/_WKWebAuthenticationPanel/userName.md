# ``WKInternalsNotes/_WKWebAuthenticationPanel/userName``

認証対象ユーザー名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy, nullable) NSString *userName;
```

## Default Value
内部の `WebAuthenticationPanel` が保持する user name に依存する。

## Discussion
`WebAuthenticationPanel::userName()` を `NSString` に変換して返す。

## References
- [`_WKWebAuthenticationPanel.h#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L179)
- [`_WKWebAuthenticationPanel.mm#L254`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L254)
- [`_WKWebAuthenticationPanel.mm#L256`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L256)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
