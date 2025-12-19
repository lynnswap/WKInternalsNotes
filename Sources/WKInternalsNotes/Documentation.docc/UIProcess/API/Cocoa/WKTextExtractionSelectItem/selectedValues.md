# ``WKInternalsNotes/WKTextExtractionSelectItem/selectedValues``

選択値の配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<NSString *> *selectedValues;
```

## Default Value
`init(selectedValues:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let selectedValues` として保持し、`init(selectedValues:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L168](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L168)
- [_WKTextExtraction.swift#L396](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L396)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
