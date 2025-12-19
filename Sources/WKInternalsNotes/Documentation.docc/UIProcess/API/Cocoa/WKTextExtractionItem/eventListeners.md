# ``WKInternalsNotes/WKTextExtractionItem/eventListeners``

イベントリスナー種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKTextExtractionEventListenerTypes eventListeners;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let eventListeners` を保持し、`init(with:)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L117](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L117)
- [_WKTextExtraction.swift#L39](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L39)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
