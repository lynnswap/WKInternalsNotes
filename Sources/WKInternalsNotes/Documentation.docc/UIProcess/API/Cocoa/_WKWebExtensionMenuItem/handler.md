# ``WKInternalsNotes/_WKWebExtensionMenuItem/handler``

`_handler` にコピー保持され、`_performAction:` から実行される。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) WebExtensionMenuItemHandlerBlock handler;
```

## Default Value
`initWithTitle:handler:` でコピーされる（それ以外は `nil` のまま）。

## Discussion
`copy` 属性のためブロックはコピーされ、`_performAction:` が `ASSERT` 後に `_handler(sender)` を実行する。`copyWithZone:` でも `_handler` をコピーする。

## References
- [`WebExtensionMenuItem.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionMenuItem.h#L56)
- [`WebExtensionMenuItemCocoa.mm#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionMenuItemCocoa.mm#L64)
- [`WebExtensionMenuItemCocoa.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionMenuItemCocoa.mm#L69)
- [`WebExtensionMenuItemCocoa.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionMenuItemCocoa.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
