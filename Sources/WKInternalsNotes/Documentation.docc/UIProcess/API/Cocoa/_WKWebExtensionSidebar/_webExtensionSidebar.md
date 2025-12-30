# ``WKInternalsNotes/_WKWebExtensionSidebar/_webExtensionSidebar``

内部の `WebKit::WebExtensionSidebar` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionSidebar& _webExtensionSidebar;
```

## Default Value
初期化後は内部 `WebExtensionSidebar` への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionSidebar` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`_WKWebExtensionSidebarInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebarInternal.h#L42)
- [`_WKWebExtensionSidebar.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L101)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
