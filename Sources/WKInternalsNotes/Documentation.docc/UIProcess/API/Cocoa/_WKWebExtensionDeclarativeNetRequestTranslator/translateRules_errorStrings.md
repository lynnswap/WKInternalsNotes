# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestTranslator/translateRules(_:errorStrings:)``

JSON ルールを WebKit 形式へ変換する。

## Objective-C Declaration
```objective-c
+ (NSArray<NSDictionary<NSString *, id> *> *)translateRules:(NSDictionary<NSString *, NSArray<NSDictionary *> *> *)jsonObjects errorStrings:(NSArray * _Nullable * _Nullable)outErrorStrings;
```

## Discussion
各ルールセットの JSON を `_WKWebExtensionDeclarativeNetRequestRule` に変換し、重複 ID や変換失敗を `errorStrings` に収集する。ルールは優先度で並べ替えた後、`ruleInWebKitFormat` を展開して返す。

## References
- [`_WKWebExtensionDeclarativeNetRequestTranslator.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.mm#L41)
- [`_WKWebExtensionDeclarativeNetRequestTranslator.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.mm#L82)
- [`_WKWebExtensionDeclarativeNetRequestTranslator.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.mm#L86)
- [`_WKWebExtensionDeclarativeNetRequestTranslator.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
