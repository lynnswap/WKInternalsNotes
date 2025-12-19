# ``WKInternalsNotes/_WKTextExtractionConfiguration/maxWordsPerParagraph``

段落あたりの最大単語数を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger maxWordsPerParagraph;
```

## Default Value
`NSUIntegerMax`。

## Discussion
段落ごとの単語数を制限し、超過分は省略される。`init` では `NSUIntegerMax` を設定する。

## References
- [`_WKTextExtraction.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L56)
- [`_WKTextExtraction.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L60)
- [`_WKTextExtraction.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
