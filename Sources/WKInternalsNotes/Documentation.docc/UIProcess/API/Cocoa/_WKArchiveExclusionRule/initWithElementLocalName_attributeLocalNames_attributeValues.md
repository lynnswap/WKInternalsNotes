# ``WKInternalsNotes/_WKArchiveExclusionRule/initWithElementLocalName(_:attributeLocalNames:attributeValues:)``

アーカイブ除外ルールを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithElementLocalName:(NSString*)elementLocalName attributeLocalNames:(NSArray<NSString *> *)attributeLocalNames attributeValues:(NSArray<NSString *> *)attributeValues;
```

## Discussion
`attributeLocalNames` と `attributeValues` の要素数が一致しない場合は例外を投げる。`elementLocalName` と `attributeLocalNames` が両方 `nil` の場合も例外になる。引数を保持して初期化する。

## References
- [`_WKArchiveExclusionRule.mm#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveExclusionRule.mm#L37)
- [`_WKArchiveExclusionRule.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKArchiveExclusionRule.h#L33)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
