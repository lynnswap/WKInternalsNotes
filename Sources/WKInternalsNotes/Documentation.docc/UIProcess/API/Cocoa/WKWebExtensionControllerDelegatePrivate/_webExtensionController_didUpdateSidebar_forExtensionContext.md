# ``WKInternalsNotes/WKWebExtensionControllerDelegatePrivate/_webExtensionController(_:didUpdateSidebar:forExtensionContext:)``

サイドバーのプロパティ更新を通知する。

## Objective-C Declaration
```objective-c
- (void)_webExtensionController:(WKWebExtensionController * _Nonnull)controller didUpdateSidebar:(_WKWebExtensionSidebar * _Nonnull)sidebar forExtensionContext:(WKWebExtensionContext * _Nonnull)context;
```

## Discussion
`WebExtensionSidebar::notifyDelegateOfPropertyUpdate` で delegate が実装していれば呼び出される。

## References
- [`WKWebExtensionControllerDelegatePrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerDelegatePrivate.h#L115)
- [`WebExtensionSidebarCocoa.mm#L529`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionSidebarCocoa.mm#L529)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
