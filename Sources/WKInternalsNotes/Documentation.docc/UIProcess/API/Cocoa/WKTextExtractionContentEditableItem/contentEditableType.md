# ``WKInternalsNotes/WKTextExtractionContentEditableItem/contentEditableType``

contenteditable の種別を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKTextExtractionEditableType contentEditableType;
```

## Default Value
`init` の引数で与えた `contentEditableType` が保持される。

## Discussion
Swift の `@_objcImplementation` extension で `contentEditableType` を保持し、初期化時に引数から設定される。

## References
- [`_WKTextExtractionInternal.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L135)
- [`_WKTextExtraction.swift#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L99)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
