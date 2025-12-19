# ``WKInternalsNotes/WKTextExtractionResult/rootItem``

抽出結果のルートアイテムを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKTextExtractionItem *rootItem;
```

## Default Value
`init(rootItem:)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let rootItem` として保持し、`init(rootItem:)` で設定される。

## References
- [_WKTextExtractionInternal.h#L180](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L180)
- [_WKTextExtraction.swift#L464](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L464)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
