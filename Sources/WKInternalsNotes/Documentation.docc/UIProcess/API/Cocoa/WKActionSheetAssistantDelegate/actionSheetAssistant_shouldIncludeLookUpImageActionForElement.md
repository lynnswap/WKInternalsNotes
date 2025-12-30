# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistant(_:shouldIncludeLookUpImageActionForElement:)``

画像のビジュアル検索アクションを含めるか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)actionSheetAssistant:(WKActionSheetAssistant *)assistant shouldIncludeLookUpImageActionForElement:(_WKActivatedElementInfo *)element;
```

## Discussion
`WebKit::isLiveTextAvailableAndEnabled()` と `hasVisualSearchResultsForImageContextMenu` の両方が true の場合に `YES` を返す。

## References
- [`WKActionSheetAssistant.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L63)
- [`WKContentViewInteraction.mm#L12924`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L12924)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
