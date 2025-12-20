# ``WKInternalsNotes/_WKWebPushDaemonConnection/getPushPermissionStateForOrigin(_:completionHandler:)``

指定 Origin の Push 許可状態を取得する。

## Objective-C Declaration
```objective-c
- (void)getPushPermissionStateForOrigin:(NSURL *)origin completionHandler:(void (^)(_WKWebPushPermissionState))completionHandler;
```

## Discussion
`_protectedConnection` の `getPushPermissionState` を呼び出し、結果の `WebCore::PushPermissionState` を `_WKWebPushPermissionState` に変換して `completionHandler` に渡す。

## References
- [`_WKWebPushDaemonConnection.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L59)
- [`_WKWebPushDaemonConnection.mm#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L114)
- [`_WKWebPushDaemonConnection.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L116)
- [`_WKWebPushDaemonConnection.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L117)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
