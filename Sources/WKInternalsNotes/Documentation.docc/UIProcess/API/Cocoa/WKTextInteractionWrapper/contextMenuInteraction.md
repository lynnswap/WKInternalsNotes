# ``WKInternalsNotes/WKTextInteractionWrapper/contextMenuInteraction``

テキスト選択用の `UIContextMenuInteraction` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, readonly) UIContextMenuInteraction *contextMenuInteraction;
```

## Default Value
`_asyncTextInteraction` がある場合はその context menu、なければ `_textInteractionAssistant` のもの。

## Discussion
`USE(UICONTEXTMENU)` 環境で、`BETextInteraction` の context menu を優先して返す。

## References
- [`WKTextInteractionWrapper.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.h#L68)
- [`WKTextInteractionWrapper.mm#L497`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTextInteractionWrapper.mm#L497)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
