# ``WKInternalsNotes/WKContentRuleListStore/_invalidateContentRuleListHeaderForIdentifier(_:)``

指定 identifier のルールリストヘッダを無効化するテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_invalidateContentRuleListHeaderForIdentifier:(NSString *)identifier;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::invalidateContentRuleListHeader` を呼び、ヘッダの無効化処理を行う。無効時は何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L35)
- [`WKContentRuleListStore.mm#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L192)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
