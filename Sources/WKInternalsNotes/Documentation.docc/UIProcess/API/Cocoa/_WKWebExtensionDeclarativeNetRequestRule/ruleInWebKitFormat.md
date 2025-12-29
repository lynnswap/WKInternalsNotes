# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/ruleInWebKitFormat``

WebKit 形式のルール配列に変換して返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<NSDictionary<NSString *, id> *> *ruleInWebKitFormat;
```

## Default Value
`action`/`condition` に基づいて都度生成される。

## Discussion
Chrome の action type を WebKit の action type に変換し、`condition` の内容に応じてルールを分割・生成する。除外ドメインやリクエストメソッドがある場合は複数ルールを返す。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L780`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L780)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
