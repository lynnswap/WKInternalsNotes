# ``WKInternalsNotes/WKTextExtractionSelectItem/supportsMultiple``

複数選択に対応するかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL supportsMultiple;
```

## Default Value
`init(supportsMultiple:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let supportsMultiple` として保持し、`init(supportsMultiple:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L169](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L169)
- [_WKTextExtraction.swift#L397](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L397)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
