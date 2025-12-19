# ``WKInternalsNotes/WKTextInteractionWrapper/scheduleReplacementsForText(_:)``

置換候補を表示する。

## Objective-C Declaration
```objective-c
- (void)scheduleReplacementsForText:(NSString *)text;
```

## Discussion
`_textInteractionAssistant scheduleReplacementsForText:` を呼び、`USE(BROWSERENGINEKIT)` では `showReplacementsForText:` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L51)
- [`WKTextInteractionWrapper.mm#L435`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L435)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
