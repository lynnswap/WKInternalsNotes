# ``WKInternalsNotes/WKTextExtractionTextItem/editable``

編集可能情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) WKTextExtractionEditable *editable;
```

## Default Value
`init(editable:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let editable` に保持し、`init(editable:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L156](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L156)
- [_WKTextExtraction.swift#L328](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L328)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
