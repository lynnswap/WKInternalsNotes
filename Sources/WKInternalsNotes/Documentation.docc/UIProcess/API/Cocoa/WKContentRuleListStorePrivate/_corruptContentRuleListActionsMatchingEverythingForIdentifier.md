# ``WKInternalsNotes/WKContentRuleListStore/_corruptContentRuleListActionsMatchingEverythingForIdentifier(_:)``

指定 identifier のアクションを全マッチ状態に破損させるテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_corruptContentRuleListActionsMatchingEverythingForIdentifier:(NSString *)identifier;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::corruptContentRuleListActionsMatchingEverything` を呼び、ルールのアクションを「すべてにマッチする」状態へ破損させる。無効時は何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L34)
- [`WKContentRuleListStore.mm#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L185)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
