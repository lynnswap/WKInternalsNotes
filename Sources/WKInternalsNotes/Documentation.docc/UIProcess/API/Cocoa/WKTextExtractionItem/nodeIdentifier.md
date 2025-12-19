# ``WKInternalsNotes/WKTextExtractionItem/nodeIdentifier``

ノード識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSString *nodeIdentifier;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let nodeIdentifier` を保持し、`init(with:)` の引数から設定される。 ヘッダコメントのとおり、将来的に UI 側のノードハンドルへ置き換える想定。

## References
- [_WKTextExtractionInternal.h#L120](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L120)
- [_WKTextExtraction.swift#L42](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L42)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
