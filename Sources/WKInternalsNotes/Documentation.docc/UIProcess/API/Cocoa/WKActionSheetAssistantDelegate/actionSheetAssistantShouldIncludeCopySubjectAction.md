# ``WKInternalsNotes/WKActionSheetAssistantDelegate/actionSheetAssistantShouldIncludeCopySubjectAction(_:)``

被写体コピーアクションを含めるか判定する。

## Objective-C Declaration
```objective-c
- (BOOL)actionSheetAssistantShouldIncludeCopySubjectAction:(WKActionSheetAssistant *)assistant;
```

## Discussion
`copySubjectResultForImageContextMenu` が存在する場合に `YES` を返す。

## References
- [`WKActionSheetAssistant.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L90)
- [`WKContentViewInteraction.mm#L13322`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L13322)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
