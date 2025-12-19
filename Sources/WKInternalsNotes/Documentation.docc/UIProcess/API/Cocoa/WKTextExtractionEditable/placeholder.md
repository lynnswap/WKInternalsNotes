# ``WKInternalsNotes/WKTextExtractionEditable/placeholder``

編集可能要素のプレースホルダを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *placeholder;
```

## Default Value
`init(placeholder:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let placeholder` として保持し、`init(label:placeholder:isSecure:isFocused:)` で設定される。

## References
- [_WKTextExtractionInternal.h#L109](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L109)
- [_WKTextExtraction.swift#L230](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L230)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
