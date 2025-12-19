# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/isChecked``

チェック状態を返す。

## Swift Declaration
```swift
var isChecked: Bool
```

## Default Value
`init(...isChecked:...)` の引数値が `backingIsChecked` に保持される。

## Discussion
Swift 実装では `backingIsChecked` を保持し、`@objc(checked)` の getter がその値を返す。

## References
- [_WKTextExtractionInternal.h#L150](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L150)
- [_WKTextExtraction.swift#L185](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L185)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
