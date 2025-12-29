# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestTranslator/jsonObjectsFromData(_:errorStrings:)``

ルールセット JSON データを辞書に変換する。

## Objective-C Declaration
```objective-c
+ (NSDictionary<NSString *, NSArray<NSDictionary *> *> *)jsonObjectsFromData:(NSDictionary<NSString *, NSData *> *)jsonData errorStrings:(NSArray * _Nullable * _Nullable)outErrorStrings;
```

## Discussion
各 `rulesetID` の `NSData` を JSON として解析し、トップレベルが配列の場合のみ結果に追加する。解析エラーの説明を収集し、`outErrorStrings` に返す。

## References
- [`_WKWebExtensionDeclarativeNetRequestTranslator.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.mm#L95)
- [`_WKWebExtensionDeclarativeNetRequestTranslator.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestTranslator.h#L34)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
