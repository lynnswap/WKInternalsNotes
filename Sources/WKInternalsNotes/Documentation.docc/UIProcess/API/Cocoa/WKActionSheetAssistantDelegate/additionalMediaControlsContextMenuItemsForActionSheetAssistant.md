# ``WKInternalsNotes/WKActionSheetAssistantDelegate/additionalMediaControlsContextMenuItemsForActionSheetAssistant(_:)``

追加のメディア制御コンテキストメニュー項目を返す。

## Objective-C Declaration
```objective-c
- (NSArray<UIMenuElement *> *)additionalMediaControlsContextMenuItemsForActionSheetAssistant:(WKActionSheetAssistant *)assistant;
```

## Discussion
visionOS でフルスクリーン中の場合は `fullScreenWindowSceneDimmingAction` を 1 件返し、それ以外は空配列を返す。

## References
- [`WKActionSheetAssistant.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L97)
- [`WKContentViewInteraction.mm#L10166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
