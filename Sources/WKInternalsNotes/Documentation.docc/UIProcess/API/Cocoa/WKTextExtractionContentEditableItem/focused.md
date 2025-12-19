# ``WKInternalsNotes/WKTextExtractionContentEditableItem/focused``

フォーカス状態を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isFocused) BOOL focused;
```

## Default Value
`init` に渡した `isFocused` が保持される。

## Discussion
Swift extension の `backingIsFocused` を `@objc(focused)` の getter で返す。

## References
- [`_WKTextExtractionInternal.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L111)
- [`_WKTextExtraction.swift#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
