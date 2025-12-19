# ``WKInternalsNotes/WKContentView/contextMenuInteraction``

コンテキストメニュー用の `UIContextMenuInteraction` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIContextMenuInteraction *contextMenuInteraction;
```

## Default Value
`USE(UICONTEXTMENU)` のとき `_textInteractionWrapper` のものを返す。

## Discussion
`USE(UICONTEXTMENU)` が有効な場合に `[_textInteractionWrapper contextMenuInteraction]` を返す。

## References
- [`WKContentViewInteraction.h#L455`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L455)
- [`WKContentViewInteraction.mm#L14741`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14741)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
