# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/placeholder``

フォームコントロールのプレースホルダを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *placeholder;
```

## Default Value
`editable` の `placeholder` をそのまま返す。

## Discussion
Swift 実装では `editable.placeholder` を返す。

## References
- [_WKTextExtractionInternal.h#L143](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L143)
- [_WKTextExtraction.swift#L159](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
