# ``WKInternalsNotes/WKTextInteractionWrapper/selectWord()``

単語単位の選択を行う。

## Objective-C Declaration
```objective-c
- (void)selectWord;
```

## Discussion
`_textInteractionAssistant selectWord` を呼ぶ。`USE(BROWSERENGINEKIT)` では次の選択変更で edit menu を表示するためフラグを立てる。

## References
- [`WKTextInteractionWrapper.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L55)
- [`WKTextInteractionWrapper.mm#L459`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L459)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
