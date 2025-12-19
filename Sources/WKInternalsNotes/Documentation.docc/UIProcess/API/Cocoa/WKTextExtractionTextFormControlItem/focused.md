# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/focused``

フォーカス状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isFocused) BOOL focused;
```

## Default Value
`editable.isFocused` の値を返す。

## Discussion
`WKTextExtractionEditable` に保持された `isFocused` を返す。

## References
- [`_WKTextExtractionInternal.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L111)
- [`_WKTextExtraction.swift#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
