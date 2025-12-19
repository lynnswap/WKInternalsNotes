# ``WKInternalsNotes/_WKTextExtractionConfiguration/shouldFilterText``

テキストのフィルタリングを行うかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL shouldFilterText;
```

## Default Value
`YES`。

## Discussion
抽出テキストのフィルタリングを有効化し、`init` で `YES` を設定する。

## References
- [`_WKTextExtractionInternal.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L53)
- [`_WKTextExtractionInternal.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L56)
- [`_WKTextExtraction.mm#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L41)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
