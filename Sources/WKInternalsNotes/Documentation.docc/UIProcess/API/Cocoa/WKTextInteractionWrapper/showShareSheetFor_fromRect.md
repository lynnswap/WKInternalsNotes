# ``WKInternalsNotes/WKTextInteractionWrapper/showShareSheetFor(_:fromRect:)``

選択語句の共有シートを表示する。

## Objective-C Declaration
```objective-c
- (void)showShareSheetFor:(NSString *)selectedTerm fromRect:(CGRect)presentationRect;
```

## Discussion
`_textInteractionAssistant showShareSheetFor:fromRect:` を呼び、`USE(BROWSERENGINEKIT)` では `shareText:fromRect:` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L49)
- [`WKTextInteractionWrapper.mm#L419`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L419)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
