# ``WKInternalsNotes/_WKWebExtensionDeclarativeNetRequestRule/compare(_:)``

ルール同士の優先度を比較する。

## Objective-C Declaration
```objective-c
- (NSComparisonResult)compare:(_WKWebExtensionDeclarativeNetRequestRule *)rule;
```

## Discussion
`priority` の高い順（大きいほど先）に並べ、同値の場合は action type の優先度で比較する。

## References
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L1209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L1209)
- [`_WKWebExtensionDeclarativeNetRequestRule.mm#L1224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.mm#L1224)
- [`_WKWebExtensionDeclarativeNetRequestRule.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Extensions/Cocoa/_WKWebExtensionDeclarativeNetRequestRule.h#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
