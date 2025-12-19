# ``WKInternalsNotes/WKTextExtractionEditable/isSecure``

セキュア入力かどうかを返す。

## Swift Declaration
```swift
var isSecure: Bool
```

## Default Value
`init(...isSecure:...)` の引数値が `backingIsSecure` に保持される。

## Discussion
Swift 実装では `backingIsSecure` を保持し、`@objc(secure)` の getter がその値を返す。

## References
- [_WKTextExtractionInternal.h#L110](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L110)
- [_WKTextExtraction.swift#L236](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L236)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
