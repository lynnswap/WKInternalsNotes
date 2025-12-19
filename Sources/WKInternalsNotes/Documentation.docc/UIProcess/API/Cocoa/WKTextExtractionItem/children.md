# ``WKInternalsNotes/WKTextExtractionItem/children``

子アイテム一覧を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<WKTextExtractionItem *> *children;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let children` を保持し、`init(with:)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L115](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L115)
- [_WKTextExtraction.swift#L38](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L38)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
