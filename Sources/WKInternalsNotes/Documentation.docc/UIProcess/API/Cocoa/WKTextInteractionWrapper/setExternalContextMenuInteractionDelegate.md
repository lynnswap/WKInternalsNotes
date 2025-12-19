# ``WKInternalsNotes/WKTextInteractionWrapper/setExternalContextMenuInteractionDelegate(_:)``

コンテキストメニューの delegate を外部から設定する。

## Objective-C Declaration
```objective-c
- (void)setExternalContextMenuInteractionDelegate:(id<UIContextMenuInteractionDelegate>)delegate;
```

## Discussion
`_textInteractionAssistant` に delegate を設定し、`USE(BROWSERENGINEKIT)` の場合は `_asyncTextInteraction` にも設定する。

## References
- [`WKTextInteractionWrapper.h#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L67)
- [`WKTextInteractionWrapper.mm#L506`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L506)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
