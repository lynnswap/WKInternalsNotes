# ``WKInternalsNotes/WKActionSheetAssistant/currentlyAvailableActionTitles()``

現在表示中のアクションタイトルを列挙する。

## Objective-C Declaration
```objective-c
- (NSArray *)currentlyAvailableActionTitles;
```

## Discussion
`_interactionSheet` がなければ空配列を返し、ある場合は `actions` の `title` を配列にして返す。

## References
- [`WKActionSheetAssistant.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.h#L132)
- [`WKActionSheetAssistant.mm#L1128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheetAssistant.mm#L1128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
