# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/action``

アクション辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSDictionary *action;
```

## Default Value
`initWithDictionary:rulesetID:errorString:` で指定した値。

## Discussion
`ruleDictionary` の `action` を保持する。`type` キーが必須で、サポートされないタイプの場合は初期化が失敗する。WebKit 形式の変換に使用される。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L172)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L185)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L201)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L793`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L793)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
