# ``WKInternalsNotes/WKTextExtractionEditable/label``

編集可能要素のラベルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *label;
```

## Default Value
`init(label:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let label` として保持し、`init(label:placeholder:isSecure:isFocused:)` で設定される。

## References
- [_WKTextExtractionInternal.h#L108](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L108)
- [_WKTextExtraction.swift#L229](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L229)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
