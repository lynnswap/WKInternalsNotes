# ``WKInternalsNotes/_WKTextExtractionConfiguration/includeURLs``

URL 属性を抽出結果に含めるかどうかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL includeURLs;
```

## Default Value
`YES`。

## Discussion
`href`/`src` などの URL 属性を抽出対象に含める。`init` で `YES` を設定する。

## References
- [`_WKTextExtraction.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L44)
- [`_WKTextExtraction.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L48)
- [`_WKTextExtraction.mm#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
