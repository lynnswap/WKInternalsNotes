# ``WKInternalsNotes/WKTextExtractionItem/ariaAttributes``

ARIA 属性の辞書を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDictionary<NSString *, NSString *> *ariaAttributes;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let ariaAttributes` を保持し、`init(with:)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L118](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L118)
- [_WKTextExtraction.swift#L40](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
