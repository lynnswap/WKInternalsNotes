# ``WKInternalsNotes/_WKTextManipulationExclusionRule/initExclusion(_:forAttribute:value:)``

属性名と値に対する除外ルールを作成する。

## Objective-C Declaration
```objective-c
- (instancetype)initExclusion:(BOOL)exclusion forAttribute:(NSString *)name value:(NSString *)value;
```

## Discussion
`exclusion` フラグと `attributeName`/`attributeValue` を保持する。

## References
- [`_WKTextManipulationExclusionRule.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L34)
- [`_WKTextManipulationExclusionRule.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L50)
- [`_WKTextManipulationExclusionRule.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
