# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/isSecure``

セキュア入力かどうかを返す。

## Swift Declaration
```swift
var isSecure: Bool
```

## Default Value
`editable` の `isSecure` をそのまま返す。

## Discussion
Swift 実装では `editable.isSecure` を返す。

## References
- [_WKTextExtractionInternal.h#L144](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L144)
- [_WKTextExtraction.swift#L144](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L144)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
