# ``WKInternalsNotes/_WKTextManipulationExclusionRule/attributeValue``

対象属性値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *attributeValue;
```

## Default Value
`initExclusion:forAttribute:value:` で指定された属性値。ほかの initializer では `nil` のまま。

## Discussion
保持している `attributeValue` を返す。

## References
- [`_WKTextManipulationExclusionRule.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L40)
- [`_WKTextManipulationExclusionRule.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L50)
- [`_WKTextManipulationExclusionRule.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L83)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
