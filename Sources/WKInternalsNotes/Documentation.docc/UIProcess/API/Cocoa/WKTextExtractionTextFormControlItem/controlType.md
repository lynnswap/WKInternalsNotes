# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/controlType``

フォームコントロール種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *controlType;
```

## Default Value
`init(controlType:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let controlType` として保持し、`init(controlType:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L146](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L146)
- [_WKTextExtraction.swift#L163](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
