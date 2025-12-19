# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/secure``

セキュア入力かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isSecure) BOOL secure;
```

## Default Value
`editable.isSecure` の値を返す。

## Discussion
`WKTextExtractionEditable` に保持された `isSecure` を返す。

## References
- [`_WKTextExtractionInternal.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L110)
- [`_WKTextExtraction.swift#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L143)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
