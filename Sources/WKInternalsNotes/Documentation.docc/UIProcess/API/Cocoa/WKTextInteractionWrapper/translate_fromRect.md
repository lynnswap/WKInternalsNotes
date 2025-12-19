# ``WKInternalsNotes/WKTextInteractionWrapper/translate(_:fromRect:)``

翻訳 UI を表示する。

## Objective-C Declaration
```objective-c
- (void)translate:(NSString *)text fromRect:(CGRect)presentationRect;
```

## Discussion
`_textInteractionAssistant translate:fromRect:` を呼び、`USE(BROWSERENGINEKIT)` では `translateText:fromRect:` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L57)
- [`WKTextInteractionWrapper.mm#L451`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L451)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
