# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/autocomplete``

autocomplete 属性値を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *autocomplete;
```

## Default Value
`init(autocomplete:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let autocomplete` として保持し、`init(autocomplete:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L147](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L147)
- [_WKTextExtraction.swift#L164](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L164)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
