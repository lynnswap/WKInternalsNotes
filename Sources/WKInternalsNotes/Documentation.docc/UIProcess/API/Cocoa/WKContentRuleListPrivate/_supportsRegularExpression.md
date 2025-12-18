# ``WKInternalsNotes/WKContentRuleList/_supportsRegularExpression(_:)``

コンテンツ拡張で正規表現がサポートされるかを判定する。

## Objective-C Declaration
```objective-c
+ (BOOL)_supportsRegularExpression:(NSString *)regex WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
Content Extensions が有効な場合は `API::ContentRuleList::supportsRegularExpression` を呼び出し、無効な場合は `NO` を返す。

## References
- [`WKContentRuleListPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleListPrivate.h#L30)
- [`WKContentRuleList.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKContentRuleList.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
