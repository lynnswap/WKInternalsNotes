# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/isDisabled``

無効化されているかどうかを返す。

## Swift Declaration
```swift
var isDisabled: Bool
```

## Default Value
`init(...isDisabled:...)` の引数値が `backingIsDisabled` に保持される。

## Discussion
Swift 実装では `backingIsDisabled` を保持し、`@objc(disabled)` の getter がその値を返す。

## References
- [_WKTextExtractionInternal.h#L149](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L149)
- [_WKTextExtraction.swift#L177](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L177)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
