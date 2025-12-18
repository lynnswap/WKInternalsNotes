# ``WKInternalsNotes/WKContentRuleListStore``

WKContentRuleListStore の Objective-C private/testing API をカテゴリ別に整理した一覧。

## Topics

### WKPrivate

- ``WKInternalsNotes/WKContentRuleListStore/_corruptContentRuleListActionsMatchingEverythingForIdentifier(_:)``
- ``WKInternalsNotes/WKContentRuleListStore/_corruptContentRuleListHeaderForIdentifier(_:usingCurrentVersion:)``
- ``WKInternalsNotes/WKContentRuleListStore/_getContentRuleListSourceForIdentifier(_:completionHandler:)``
- ``WKInternalsNotes/WKContentRuleListStore/_invalidateContentRuleListHeaderForIdentifier(_:)``
- ``WKInternalsNotes/WKContentRuleListStore/_invalidateContentRuleListVersionForIdentifier(_:)``
- ``WKInternalsNotes/WKContentRuleListStore/_removeAllContentRuleLists()``
- ``WKInternalsNotes/WKContentRuleListStore/_setContentRuleListStoreForResourceMonitorURLsControllerForTesting(_:)``
- ``WKInternalsNotes/WKContentRuleListStore/defaultStoreWithLegacyFilename()``
- ``WKInternalsNotes/WKContentRuleListStore/storeWithURLAndLegacyFilename(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKContentRuleListStorePrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h) |
