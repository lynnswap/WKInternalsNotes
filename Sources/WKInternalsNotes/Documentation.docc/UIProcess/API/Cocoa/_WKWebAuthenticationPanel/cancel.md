# ``WKInternalsNotes/_WKWebAuthenticationPanel/cancel()``

進行中の Web Authentication をキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancel;
```

## Discussion
`ENABLE(WEB_AUTHN)` の場合は `API::WebAuthenticationPanel::cancel` に委譲する。

## References
- [`_WKWebAuthenticationPanel.h#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.h#L173)
- [`_WKWebAuthenticationPanel.mm#L812`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L812)
- [`_WKWebAuthenticationPanel.mm#L815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebAuthenticationPanel.mm#L815)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
