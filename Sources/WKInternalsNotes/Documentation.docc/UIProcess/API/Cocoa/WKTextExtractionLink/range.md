# ``WKInternalsNotes/WKTextExtractionLink/range``

リンク範囲を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSRange range;
```

## Default Value
`init(url:range:)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let range` として保持し、`init(url:range:)` で設定される。

## References
- [_WKTextExtractionInternal.h#L103](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L103)
- [_WKTextExtraction.swift#L309](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L309)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
