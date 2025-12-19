# ``WKInternalsNotes/_WKTextManipulationExclusionRule/initExclusion(_:forElement:)``

要素名に対する除外ルールを作成する。

## Objective-C Declaration
```objective-c
- (instancetype)initExclusion:(BOOL)exclusion forElement:(NSString *)localName;
```

## Discussion
`exclusion` フラグと `elementName` を保持する。

## References
- [`_WKTextManipulationExclusionRule.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L33)
- [`_WKTextManipulationExclusionRule.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L39)
- [`_WKTextManipulationExclusionRule.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
