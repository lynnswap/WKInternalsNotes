# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/ruleID``

ルールの ID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSInteger ruleID;
```

## Default Value
`initWithDictionary:rulesetID:errorString:` で指定した値。

## Discussion
`ruleDictionary` の `id` を `NSInteger` として保持する。`id` が欠落または 1 未満の場合は初期化が失敗する。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L137)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L158)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
