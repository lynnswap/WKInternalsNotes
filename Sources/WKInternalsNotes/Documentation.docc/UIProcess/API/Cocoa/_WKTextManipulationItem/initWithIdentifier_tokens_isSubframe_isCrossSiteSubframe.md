# ``WKInternalsNotes/_WKTextManipulationItem/initWithIdentifier(_:tokens:isSubframe:isCrossSiteSubframe:)``

識別子とトークン列に加えてサブフレーム情報を設定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithIdentifier:(nullable NSString *)identifier tokens:(NSArray<_WKTextManipulationToken *> *)tokens isSubframe:(BOOL)isSubframe isCrossSiteSubframe:(BOOL)isCrossSiteSubframe WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
`identifier`/`tokens` に加えて `isSubframe` と `isCrossSiteSubframe` を保持する。

## References
- [`_WKTextManipulationItem.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L38)
- [`_WKTextManipulationItem.mm#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L50)
- [`_WKTextManipulationItem.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L55)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
