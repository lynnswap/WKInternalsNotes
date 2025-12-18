# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:presentSidebar:forExtensionContext:completionHandler:)``

拡張がサイドバー表示を要求したときに呼び出される。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller presentSidebar:(_WKWebExtensionSidebar * _Nonnull)sidebar forExtensionContext:(WKWebExtensionContext * _Nonnull)context completionHandler:(void (^)(NSError * _Nullable error))completionHandler;
```

## Discussion
`WebExtensionContext::openSidebar` から、controller/delegate/wrapper が揃っている場合に呼び出される。`completionHandler` は空のブロックで渡される。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L97)
- [`WebExtensionContextAPISidebarCocoa.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/API/WebExtensionContextAPISidebarCocoa.mm#L126)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
