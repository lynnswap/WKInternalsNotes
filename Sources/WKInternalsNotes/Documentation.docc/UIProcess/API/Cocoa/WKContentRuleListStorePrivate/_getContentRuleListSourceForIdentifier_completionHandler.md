# ``WKInternalsNotes/WKContentRuleListStore/_getContentRuleListSourceForIdentifier(_:completionHandler:)``

指定 identifier のルールリストソース文字列を取得してハンドラに返すテスト用 API。

## Objective-C Declaration
```objective-c
- (void)_getContentRuleListSourceForIdentifier:(NSString *)identifier completionHandler:(void (^)(NSString *))completionHandler;
```

## Discussion
`ENABLE(CONTENT_EXTENSIONS)` の場合に completionHandler を `copy` し、`API::ContentRuleListStore::getContentRuleListSource` の結果を `NSString` に変換して返す。戻り値の `String` が null の場合は `nil` を渡すため、nonnull 警告を一時的に抑制している。無効時は処理しない。

## References
- [`WKContentRuleListStorePrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStorePrivate.h#L36)
- [`WKContentRuleListStore.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListStore.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
