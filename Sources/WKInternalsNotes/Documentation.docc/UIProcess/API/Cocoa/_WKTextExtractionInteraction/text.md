# ``WKInternalsNotes/_WKTextExtractionInteraction/text``

操作に渡すテキストを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSString *text;
```

## Default Value
`nil`。

## Discussion
setter は `copy` した値を保持し、getter は保持している文字列を返す。

## References
- [`_WKTextExtraction.mm#L81`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L81)
- [`_WKTextExtraction.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L86)
- [`_WKTextExtraction.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
