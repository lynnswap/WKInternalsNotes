# ``WKInternalsNotes/_WKWebExtensionKeyCommand/commandWithTitle(_:image:input:modifierFlags:identifier:)``

Web 拡張用の `UIKeyCommand` を生成する。

## Objective-C Declaration
```objective-c
+ (UIKeyCommand *)commandWithTitle:(NSString *)title image:(UIImage *)image input:(NSString *)input modifierFlags:(UIKeyModifierFlags)modifierFlags identifier:(NSString *)identifier;
```

## Discussion
`title`/`input`/`identifier` を `RELEASE_ASSERT` で検証し、`propertyList` にそれぞれ格納して `UIKeyCommand` を作成する。生成に失敗した場合は `nil` を返す。

## References
- [`WebExtensionCommand.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/WebExtensionCommand.h#L55)
- [`WebExtensionCommandCocoa.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/WebExtensionCommandCocoa.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
