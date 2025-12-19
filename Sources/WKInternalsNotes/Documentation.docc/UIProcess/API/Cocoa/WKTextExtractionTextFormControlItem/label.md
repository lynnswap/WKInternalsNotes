# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/label``

フォームコントロールのラベルを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *label;
```

## Default Value
`editable` の `label` をそのまま返す。

## Discussion
Swift 実装では `editable.label` を返す。

## References
- [_WKTextExtractionInternal.h#L142](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L142)
- [_WKTextExtraction.swift#L154](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
