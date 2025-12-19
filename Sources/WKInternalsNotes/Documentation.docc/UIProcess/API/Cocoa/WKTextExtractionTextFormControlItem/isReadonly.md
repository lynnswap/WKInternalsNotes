# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/isReadonly``

読み取り専用かどうかを返す。

## Swift Declaration
```swift
var isReadonly: Bool
```

## Default Value
`init(...isReadonly:...)` の引数値が `backingIsReadonly` に保持される。

## Discussion
Swift 実装では `backingIsReadonly` を保持し、`@objc(readonly)` の getter がその値を返す。

## References
- [_WKTextExtractionInternal.h#L148](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L148)
- [_WKTextExtraction.swift#L169](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
