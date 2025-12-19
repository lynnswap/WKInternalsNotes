# ``WKInternalsNotes/_WKTextExtractionConfiguration/canIncludeIdentifiers``

インタラクティブ要素の識別子を含めるかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL canIncludeIdentifiers;
```

## Default Value
`YES`。

## Discussion
各要素のユニーク識別子を含めるかどうかを制御し、`init` で `YES` を設定する。

## References
- [`_WKTextExtractionInternal.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L47)
- [`_WKTextExtractionInternal.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L51)
- [`_WKTextExtraction.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
