# ``WKInternalsNotes/WKContentRuleList/_parseRuleList(_:)``

ルールリスト文字列を解析し、失敗時は NSError を返す。

## Objective-C Declaration
```objective-c
+ (NSError *)_parseRuleList:(NSString *)ruleList WK_API_AVAILABLE(macos(13.4), ios(16.5));
```

## Discussion
`API::ContentRuleList::parseRuleList` を実行し、エラーがあれば `WKErrorDomain` / `WKErrorContentRuleListStoreCompileFailed` で `NSError` を返す。成功時は `nil` を返し、Content Extensions が無効な場合も `nil` になる。

## References
- [`WKContentRuleListPrivate.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListPrivate.h#L31)
- [`WKContentRuleList.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleList.mm#L75)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
