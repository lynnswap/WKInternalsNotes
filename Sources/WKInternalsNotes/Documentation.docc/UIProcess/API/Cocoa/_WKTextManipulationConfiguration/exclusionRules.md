# ``WKInternalsNotes/_WKTextManipulationConfiguration/exclusionRules``

除外ルール配列を保持する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSArray<_WKTextManipulationExclusionRule *> *exclusionRules;
```

## Default Value
自動合成された `_exclusionRules` の値。

## Discussion
`dealloc` で `_exclusionRules` を release する以外の追加処理は無い。

## References
- [`_WKTextManipulationConfiguration.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationConfiguration.h#L34)
- [`_WKTextManipulationConfiguration.mm#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationConfiguration.mm#L31)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
