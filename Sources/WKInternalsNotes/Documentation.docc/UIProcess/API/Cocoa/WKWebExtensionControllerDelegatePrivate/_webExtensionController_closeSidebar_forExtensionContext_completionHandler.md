# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:closeSidebar:forExtensionContext:completionHandler:)``

拡張がサイドバーを閉じる要求をしたときに呼び出される。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller closeSidebar:(_WKWebExtensionSidebar * _Nonnull)sidebar forExtensionContext:(WKWebExtensionContext * _Nonnull)context completionHandler:(void (^)(NSError * _Nullable error))completionHandler;
```

## Discussion
`WebExtensionContext::closeSidebar` から、controller/delegate/wrapper が揃っている場合に呼び出される。`completionHandler` は空のブロックで渡される。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L107)
- [`WebExtensionContextAPISidebarCocoa.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPISidebarCocoa.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
