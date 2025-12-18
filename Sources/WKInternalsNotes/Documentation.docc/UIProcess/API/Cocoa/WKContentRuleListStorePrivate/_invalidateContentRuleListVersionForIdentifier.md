# ``WKInternalsNotes/WKContentRuleListStore/_invalidateContentRuleListVersionForIdentifier(_:)``

指定 identifier のルールリストのバージョン情報を無効化するテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_invalidateContentRuleListVersionForIdentifier:(NSString *)identifier;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::invalidateContentRuleListVersion` を呼び出してバージョン情報を無効化する。無効時は何もしない。

## References
- [`WKContentRuleListStorePrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L32)
- [`WKContentRuleListStore.mm#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L171)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
