# ``WKInternalsNotes/WKTextInteractionWrapper/scheduleChineseTransliterationForText(_:)``

中国語の翻字候補を表示する。

## Objective-C Declaration
```objective-c
- (void)scheduleChineseTransliterationForText:(NSString *)text;
```

## Discussion
`_textInteractionAssistant scheduleChineseTransliterationForText:` を呼び、`USE(BROWSERENGINEKIT)` では `transliterateChineseForText:` を呼ぶ。

## References
- [`WKTextInteractionWrapper.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L52)
- [`WKTextInteractionWrapper.mm#L443`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L443)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
