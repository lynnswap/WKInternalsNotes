# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/priority``

ルールの優先度を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSInteger priority;
```

## Default Value
`ruleDictionary` に指定がなければ `1`。

## Discussion
`priority` があればその値を使い、無ければ `1` を設定する。`priority` が 1 未満の場合は初期化が失敗する。比較時は優先度の高い順に並べ替える。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L155)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L165`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L165)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L1209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L1209)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
