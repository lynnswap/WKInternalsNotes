# ``WKInternalsNotes/_WKTextManipulationExclusionRule/elementName``

対象要素名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *elementName;
```

## Default Value
`initExclusion:forElement:` で指定された要素名。ほかの initializer では `nil` のまま。

## Discussion
保持している `elementName` を返す。

## References
- [`_WKTextManipulationExclusionRule.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L38)
- [`_WKTextManipulationExclusionRule.mm#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L39)
- [`_WKTextManipulationExclusionRule.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L73)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
