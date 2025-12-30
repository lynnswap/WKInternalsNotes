# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:decideActionsForElement:defaultActions:)``

表示するアクション一覧を決定する。

## Objective-C Declaration
```objective-c
- (RetainPtr<NSArray>)actionSheetAssistant:(WKActionSheetAssistant *)assistant decideActionsForElement:(_WKActivatedElementInfo *)element defaultActions:(RetainPtr<NSArray>)defaultActions;
```

## Discussion
`_page->uiClient().actionsForElement` を呼び、デフォルトアクションを加工した結果を返す。

## References
- [`WKActionSheetAssistant.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L59)
- [`WKContentViewInteraction.mm#L10084`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10084)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
