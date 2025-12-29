# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/rulesetID``

ルールセット識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *rulesetID;
```

## Default Value
`initWithDictionary:rulesetID:errorString:` で指定した値。

## Discussion
初期化時に渡された `rulesetID` を保持する。WebKit 形式ルール変換時、条件によって `_rulesetIdentifier` として出力される。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L145`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L145)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L887`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L887)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
