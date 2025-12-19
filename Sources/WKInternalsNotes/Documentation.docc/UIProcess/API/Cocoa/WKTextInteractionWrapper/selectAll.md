# ``WKInternalsNotes/WKTextInteractionWrapper/selectAll(_:)``

全選択を行う。

## Objective-C Declaration
```objective-c
- (void)selectAll:(id)sender;
```

## Discussion
`_textInteractionAssistant selectAll:` を呼ぶ。`USE(BROWSERENGINEKIT)` では次の選択変更で edit menu を表示するためフラグを立てる。

## References
- [`WKTextInteractionWrapper.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L56)
- [`WKTextInteractionWrapper.mm#L467`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L467)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
