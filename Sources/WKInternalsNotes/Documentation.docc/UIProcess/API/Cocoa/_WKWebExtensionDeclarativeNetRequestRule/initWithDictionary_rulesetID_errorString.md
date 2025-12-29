# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/initWithDictionary(_:rulesetID:errorString:)``

ルール辞書から宣言的ネットリクエスト規則を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDictionary:(NSDictionary *)ruleDictionary rulesetID:(NSString *)rulesetID errorString:(NSString * _Nullable * _Nullable)outErrorString NS_DESIGNATED_INITIALIZER;
```

## Discussion
`ruleDictionary` に必須キー（`id`/`action`/`condition`）があることを検証し、`ruleID` と `rulesetID` を保持する。`priority` は省略時 1。`ruleID`/`priority` が 1 未満、未サポートの action type、`regexFilter` と `urlFilter` の併用など検証に失敗した場合は `outErrorString` を設定して `nil` を返す。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L119)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L137)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L155)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L172)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L208)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
