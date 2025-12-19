# ``WKInternalsNotes/_WKTextManipulationExclusionRule/attributeName``

対象属性名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *attributeName;
```

## Default Value
`initExclusion:forAttribute:value:` で指定された属性名。ほかの initializer では `nil` のまま。

## Discussion
保持している `attributeName` を返す。

## References
- [`_WKTextManipulationExclusionRule.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L39)
- [`_WKTextManipulationExclusionRule.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L50)
- [`_WKTextManipulationExclusionRule.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
