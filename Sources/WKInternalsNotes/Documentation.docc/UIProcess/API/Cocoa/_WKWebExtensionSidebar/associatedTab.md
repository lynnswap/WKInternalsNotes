# ``WKInternalsNotes/_WKWebExtensionSidebar/associatedTab``

関連付けられたタブを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly, weak) id <WKWebExtensionTab> associatedTab;
```

## Default Value
デフォルトサイドバーの場合は `nil`。

## Discussion
`WebExtensionSidebar::tab()` が存在すれば `tab->delegate()` を返し、未設定なら `nil` を返す。

## References
- [`_WKWebExtensionSidebar.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.h#L57)
- [`_WKWebExtensionSidebar.mm#L89`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebExtensionSidebar.mm#L89)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
