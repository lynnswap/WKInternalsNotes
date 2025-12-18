# ``WKInternalsNotes/WKContentRuleListStore/_removeAllContentRuleLists()``

コンテンツルールリストを全件同期削除するテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_removeAllContentRuleLists;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::synchronousRemoveAllContentRuleLists` を呼び、ストア内のルールリストを同期的に削除する。無効時は何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L31)
- [`WKContentRuleListStore.mm#L164`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L164)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
