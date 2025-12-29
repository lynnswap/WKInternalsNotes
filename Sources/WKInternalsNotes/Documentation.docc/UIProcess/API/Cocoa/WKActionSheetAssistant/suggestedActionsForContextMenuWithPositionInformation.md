# ``WKInternalsNotes/WKActionSheetAssistant/suggestedActionsForContextMenuWithPositionInformation(_:)``

位置情報からコンテキストメニュー用の既定アクションを生成する。

## Objective-C Declaration
```objective-c
- (NSMutableArray<UIMenuElement *> *)suggestedActionsForContextMenuWithPositionInformation:(const WebKit::InteractionInformationAtPosition&)positionInformation;
```

## Discussion
`positionInformation` から `_WKActivatedElementInfo` を作り、リンクか画像かで既定アクションを選択する。取得した `_WKElementAction` 群を `uiActionForElementInfo:` で `UIMenuElement` に変換して返す。

## References
- [`WKActionSheetAssistant.h#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L127)
- [`WKActionSheetAssistant.mm#L904`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L904)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
