# ``WKInternalsNotes/_WKWebAuthenticationPanel/init()``

Web Authentication パネルを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)init;
```

## Discussion
`WebAuthenticationPanel` の API ラッパーを `self` に構築して初期化する（`ENABLE(WEB_AUTHN)` の場合）。

## References
- [`_WKWebAuthenticationPanel.h#L164`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L164)
- [`_WKWebAuthenticationPanel.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L140)
- [`_WKWebAuthenticationPanel.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L145)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
