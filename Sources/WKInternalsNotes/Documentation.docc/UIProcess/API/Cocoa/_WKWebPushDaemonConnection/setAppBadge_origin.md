# ``WKInternalsNotes/_WKWebPushDaemonConnection/setAppBadge(_:origin:)``

アプリバッジを設定する。

## Objective-C Declaration
```objective-c
- (void)setAppBadge:(NSUInteger *)badge origin:(NSURL *)origin;
```

## Discussion
`badge` が `nil` の場合は `std::nullopt` を渡し、`nil` でない場合は `uint64_t` に変換して `setAppBadge` に渡す。

## References
- [`_WKWebPushDaemonConnection.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L61)
- [`_WKWebPushDaemonConnection.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L128)
- [`_WKWebPushDaemonConnection.mm#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L130)
- [`_WKWebPushDaemonConnection.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L131)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
