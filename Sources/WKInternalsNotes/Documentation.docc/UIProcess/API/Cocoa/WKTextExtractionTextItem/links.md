# ``WKInternalsNotes/WKTextExtractionTextItem/links``

テキスト内リンク一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<WKTextExtractionLink *> *links;
```

## Default Value
`init(links:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let links` に保持し、`init(links:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L155](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L155)
- [_WKTextExtraction.swift#L327](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L327)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
