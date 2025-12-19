# ``WKInternalsNotes/WKTextExtractionContentEditableItem/isFocused``

contentEditable のフォーカス状態を返す。

## Swift Declaration
```swift
var isFocused: Bool
```

## Default Value
`init(contentEditableType:isFocused:...)` の引数値が `backingIsFocused` に保持される。

## Discussion
Swift 実装では `backingIsFocused` を保持し、`@objc(focused)` の getter がその値を返す。

## References
- [_WKTextExtractionInternal.h#L137](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L137)
- [_WKTextExtraction.swift#L105](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
