# ``WKInternalsNotes/WKTextExtractionTextItem/selectedRange``

選択範囲を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSRange selectedRange;
```

## Default Value
`init(selectedRange:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `var selectedRange` を保持し、`init(selectedRange:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L157](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L157)
- [_WKTextExtraction.swift#L326](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L326)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
