# ``WKInternalsNotes/WKTextInteractionWrapper/lookup(_:withRange:fromRect:)``

辞書/調べる UI を表示する。

## Objective-C Declaration
```objective-c
- (void)lookup:(NSString *)textWithContext withRange:(NSRange)range fromRect:(CGRect)presentationRect;
```

## Discussion
`_textInteractionAssistant lookup:withRange:fromRect:` を呼び、`USE(BROWSERENGINEKIT)` では `showDictionaryForTextInContext:...` も呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L48)
- [`WKTextInteractionWrapper.mm#L411`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L411)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
