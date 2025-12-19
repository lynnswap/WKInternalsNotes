# ``WKInternalsNotes/_WKTextManipulationExclusionRule/className``

対象クラス名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *className;
```

## Default Value
`initExclusion:forClass:` で指定されたクラス名。ほかの initializer では `nil` のまま。

## Discussion
保持している `className` を返す。

## References
- [`_WKTextManipulationExclusionRule.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L41)
- [`_WKTextManipulationExclusionRule.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L62)
- [`_WKTextManipulationExclusionRule.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.mm#L88)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
