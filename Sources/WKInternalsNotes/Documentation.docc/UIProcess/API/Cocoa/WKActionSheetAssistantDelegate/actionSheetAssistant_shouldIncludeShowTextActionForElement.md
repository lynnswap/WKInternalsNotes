# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:shouldIncludeShowTextActionForElement:)``

画像のテキスト表示アクションを含めるか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)actionSheetAssistant:(WKActionSheetAssistant *)assistant shouldIncludeShowTextActionForElement:(_WKActivatedElementInfo *)element;
```

## Discussion
`WebKit::isLiveTextAvailableAndEnabled()` と `hasSelectableTextForImageContextMenu` の両方が true の場合に `YES` を返す。

## References
- [`WKActionSheetAssistant.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L60)
- [`WKContentViewInteraction.mm#L12914`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12914)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
