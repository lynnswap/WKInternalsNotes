# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:queryPermission:forOrigin:completionHandler:)``

指定権限の状態を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView queryPermission:(NSString*)name forOrigin:(WKSecurityOrigin*)origin completionHandler:(void (^)(WKPermissionDecision permissionState))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
UIDelegate::UIClient が `CompletionHandlerCallChecker` を挟み、`WKPermissionDecision` を `PermissionState` に変換して callback を解決する。未実装時は Prompt を返す。

## References
- [`WKUIDelegatePrivate.h#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L158)
- [`UIDelegate.mm#L1918`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L1918)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
