# ``WKInternalsNotes/_WKTextManipulationExclusionRule/isExclusion``

除外ルールかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isExclusion;
```

## Default Value
`initExclusion:forElement:` などで渡した `exclusion` 値が保持される。

## Discussion
`exclusion` フラグをそのまま返す。

## References
- [`_WKTextManipulationExclusionRule.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L37)
- [`_WKTextManipulationExclusionRule.mm#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
