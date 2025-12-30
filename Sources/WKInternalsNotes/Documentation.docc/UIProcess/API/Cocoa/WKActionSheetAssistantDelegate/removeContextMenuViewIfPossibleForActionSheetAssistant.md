# ``WKInternalsNotes/WKActionSheetAssistantDelegate/removeContextMenuViewIfPossibleForActionSheetAssistant(_:)``

コンテキストメニューのヒントビューを撤去する。

## Objective-C Declaration
```objective-c
- (void)removeContextMenuViewIfPossibleForActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
`_removeContextMenuHintContainerIfPossible` を呼び、表示中のヒントビューを取り除く。

## References
- [`WKActionSheetAssistant.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L78)
- [`WKContentViewInteraction.mm#L10182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
