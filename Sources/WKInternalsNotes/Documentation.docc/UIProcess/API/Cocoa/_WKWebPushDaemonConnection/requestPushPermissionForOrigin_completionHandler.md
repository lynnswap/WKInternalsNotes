# ``WKInternalsNotes/_WKWebPushDaemonConnection/requestPushPermissionForOrigin(_:completionHandler:)``

指定 Origin への Push 許可を要求する。

## Objective-C Declaration
```objective-c
- (void)requestPushPermissionForOrigin:(NSURL *)origin completionHandler:(void (^)(BOOL))completionHandler;
```

## Discussion
`_protectedConnection` の `requestPushPermission` を呼び出し、結果の `bool` をそのまま `completionHandler` に渡す。

## References
- [`_WKWebPushDaemonConnection.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.h#L60)
- [`_WKWebPushDaemonConnection.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L121)
- [`_WKWebPushDaemonConnection.mm#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L123)
- [`_WKWebPushDaemonConnection.mm#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebPushDaemonConnection.mm#L124)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
