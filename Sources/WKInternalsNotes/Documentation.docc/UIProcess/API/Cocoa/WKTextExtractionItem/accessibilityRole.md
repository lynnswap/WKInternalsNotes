# ``WKInternalsNotes/WKTextExtractionItem/accessibilityRole``

アクセシビリティロールを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *accessibilityRole;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let accessibilityRole` を保持し、`init(with:)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L119](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L119)
- [_WKTextExtraction.swift#L41](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
