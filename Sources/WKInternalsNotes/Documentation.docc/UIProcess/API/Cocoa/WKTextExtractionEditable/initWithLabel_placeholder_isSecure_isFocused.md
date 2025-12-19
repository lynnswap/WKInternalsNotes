# ``WKInternalsNotes/WKTextExtractionEditable/initWithLabel(_:placeholder:isSecure:isFocused:)``

編集可能要素のラベルや状態を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithLabel:(NSString *)label placeholder:(NSString *)placeholder isSecure:(BOOL)isSecure isFocused:(BOOL)isFocused;
```

## Discussion
`label` / `placeholder` / `isSecure` / `isFocused` を保持する Swift initializer。

## References
- [`_WKTextExtractionInternal.h#L107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L107)
- [`_WKTextExtraction.swift#L250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L250)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
