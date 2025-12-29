# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/condition``

条件辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSDictionary *condition;
```

## Default Value
`initWithDictionary:rulesetID:errorString:` で指定した値。

## Discussion
`ruleDictionary` の `condition` を保持する。`regexFilter` と `urlFilter` の併用や `resourceTypes` と `excludedResourceTypes` の併用など、条件の整合性チェックに失敗した場合は初期化が失敗する。WebKit 形式の変換に使用される。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L208)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L233)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L265)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L797`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L797)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L46)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
