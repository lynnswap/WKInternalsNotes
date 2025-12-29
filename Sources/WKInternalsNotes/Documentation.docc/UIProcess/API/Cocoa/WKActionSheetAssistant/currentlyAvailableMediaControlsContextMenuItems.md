# ``WKInternalsNotes/WKActionSheetAssistant/currentlyAvailableMediaControlsContextMenuItems()``

メディアコントロール用コンテキストメニュー項目を返す。

## Objective-C Declaration
```objective-c
- (NSArray *)currentlyAvailableMediaControlsContextMenuItems;
```

## Discussion
`_mediaControlsContextMenu` がある場合はその内容を辞書化して配列に入れ、なければ空配列を返す。

## References
- [`WKActionSheetAssistant.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L134)
- [`WKActionSheetAssistant.mm#L1169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L1169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
