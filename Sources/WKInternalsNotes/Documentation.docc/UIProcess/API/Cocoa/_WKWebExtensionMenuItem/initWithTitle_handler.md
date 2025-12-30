# ``WKInternalsNotes/_WKWebExtensionMenuItem/initWithTitle(_:handler:)``

ハンドラ必須で初期化し、ターゲットとアクションを自分自身に設定する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithTitle:(NSString *)title handler:(WebExtensionMenuItemHandlerBlock)block;
```

## Discussion
`handler` の非 `nil` を `RELEASE_ASSERT` で保証し、`[super initWithTitle:action:keyEquivalent:]` を `@selector(_performAction:)` と空文字のキーボードショートカットで呼ぶ。`self.target = self` を設定し、`handler` をコピーして `_handler` に保持する。

## References
- [`WebExtensionMenuItem.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionMenuItem.h#L54)
- [`WebExtensionMenuItemCocoa.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionMenuItemCocoa.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
