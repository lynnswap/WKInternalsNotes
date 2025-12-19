# ``WKInternalsNotes/WKTextExtractionScrollableItem/contentSize``

スクロール領域の contentSize を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGSize contentSize;
```

## Default Value
`init(contentSize:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let contentSize` として保持し、`init(contentSize:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L163](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L163)
- [_WKTextExtraction.swift#L365](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L365)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
