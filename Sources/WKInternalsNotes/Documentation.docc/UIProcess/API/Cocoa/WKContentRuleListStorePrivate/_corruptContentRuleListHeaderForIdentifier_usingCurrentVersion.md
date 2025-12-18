# ``WKInternalsNotes/WKContentRuleListStore/_corruptContentRuleListHeaderForIdentifier(_:usingCurrentVersion:)``

指定 identifier のルールリストヘッダを破損させるテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_corruptContentRuleListHeaderForIdentifier:(NSString *)identifier usingCurrentVersion:(BOOL)usingCurrentVersion;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::corruptContentRuleListHeader` を呼び、`usingCurrentVersion` を渡してヘッダ破損の方法を選択する。無効時は何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L33)
- [`WKContentRuleListStore.mm#L178`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L178)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
