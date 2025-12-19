# ``WKInternalsNotes/_WKTextExtractionConfiguration/mergeParagraphs``

隣接するテキストを段落としてまとめるかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL mergeParagraphs;
```

## Default Value
`NO`。

## Discussion
隣接するテキストを段落として結合し、リンクや編集可能要素も単一のテキスト項目にまとめる。

## References
- [`_WKTextExtractionInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L34)
- [`_WKTextExtractionInternal.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
