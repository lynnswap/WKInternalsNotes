# ``WKInternalsNotes/_WKTextManipulationItem/initWithIdentifier(_:tokens:)``

識別子とトークン列で項目を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithIdentifier:(nullable NSString *)identifier tokens:(NSArray<_WKTextManipulationToken *> *)tokens;
```

## Discussion
渡された `identifier` と `tokens` をそのまま保持する。`isSubframe` と `isCrossSiteSubframe` は既定で `NO` のまま。

## References
- [`_WKTextManipulationItem.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L37)
- [`_WKTextManipulationItem.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L40)
- [`_WKTextManipulationItem.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
