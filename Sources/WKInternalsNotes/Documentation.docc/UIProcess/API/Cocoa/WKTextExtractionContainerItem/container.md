# ``WKInternalsNotes/WKTextExtractionContainerItem/container``

コンテナ種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKTextExtractionContainer container;
```

## Default Value
`init(container:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let container` に保持し、`init(container:...)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L125](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L125)
- [_WKTextExtraction.swift#L69](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
