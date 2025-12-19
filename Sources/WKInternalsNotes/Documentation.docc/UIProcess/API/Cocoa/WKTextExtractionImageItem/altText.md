# ``WKInternalsNotes/WKTextExtractionImageItem/altText``

代替テキストを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *altText;
```

## Default Value
`init(altText:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let altText` として保持し、`init(altText:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L175](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L175)
- [_WKTextExtraction.swift#L431](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L431)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
