# ``WKInternalsNotes/WKContentRuleListStore/defaultStoreWithLegacyFilename()``

レガシーファイル名を想定したデフォルトストアを返す。

## Objective-C Declaration
```objective-c
+ (instancetype)defaultStoreWithLegacyFilename;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に `API::ContentRuleListStore::defaultStoreSingleton()` をラップして返す。無効時は `nil`。レガシーファイル名の扱いは下位実装に委ねられるため、このメソッド内では追加の処理を行わない。

## References
- [`WKContentRuleListStorePrivate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L39)
- [`WKContentRuleListStore.mm#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L229)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
