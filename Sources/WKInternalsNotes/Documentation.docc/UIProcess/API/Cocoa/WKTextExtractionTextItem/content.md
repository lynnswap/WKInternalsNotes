# ``WKInternalsNotes/WKTextExtractionTextItem/content``

抽出されたテキスト内容を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy) NSString *content;
```

## Default Value
`init(content:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `var content` を保持し、`init(content:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L158](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L158)
- [_WKTextExtraction.swift#L325](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L325)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
