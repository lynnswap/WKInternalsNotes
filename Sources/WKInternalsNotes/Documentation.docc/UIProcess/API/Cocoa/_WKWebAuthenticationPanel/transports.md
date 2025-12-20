# ``WKInternalsNotes/_WKWebAuthenticationPanel/transports``

対応するトランスポートの集合を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSSet *transports;
```

## Default Value
`_panel->transports()` から初回に生成しキャッシュする。

## Discussion
`WebAuthenticationPanel` が提供する transports を `_WKWebAuthenticationTransport` に変換して `NSSet` に詰める。初回生成後は `_transports` を返す。

## References
- [`_WKWebAuthenticationPanel.h#L177`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L177)
- [`_WKWebAuthenticationPanel.mm#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L209)
- [`_WKWebAuthenticationPanel.mm#L214`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L214)
- [`_WKWebAuthenticationPanel.mm#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
