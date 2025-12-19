# ``WKInternalsNotes/WKTextInteractionWrapper/showTextServiceFor(_:fromRect:)``

テキストサービス（ショートカット追加など）を表示する。

## Objective-C Declaration
```objective-c
- (void)showTextServiceFor:(NSString *)selectedTerm fromRect:(CGRect)presentationRect;
```

## Discussion
`_textInteractionAssistant showTextServiceFor:fromRect:` を呼び、`USE(BROWSERENGINEKIT)` では `addShortcutForText:fromRect:` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L50)
- [`WKTextInteractionWrapper.mm#L427`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L427)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
