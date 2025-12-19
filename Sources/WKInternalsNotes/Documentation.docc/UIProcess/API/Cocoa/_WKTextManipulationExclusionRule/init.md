# ``WKInternalsNotes/_WKTextManipulationExclusionRule/init()``

利用できない初期化子。

## Objective-C Declaration
```objective-c
- (instancetype)init NS_UNAVAILABLE;
```

## Discussion
除外ルールは `initExclusion:forElement:` などの専用 initializer で構築する。

## References
- [`_WKTextManipulationExclusionRule.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationExclusionRule.h#L32)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
