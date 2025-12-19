# ``WKInternalsNotes/_WKTextExtractionConfiguration/includeRects``

テキストノードの矩形を自動で含めるかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL includeRects;
```

## Default Value
`YES`。

## Discussion
テキストノードのバウンディング矩形を含める。`init` で `YES` を設定する。

## References
- [`_WKTextExtraction.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L50)
- [`_WKTextExtraction.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L54)
- [`_WKTextExtraction.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
