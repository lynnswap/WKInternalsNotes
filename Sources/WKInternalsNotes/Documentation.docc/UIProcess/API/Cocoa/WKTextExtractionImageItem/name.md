# ``WKInternalsNotes/WKTextExtractionImageItem/name``

画像名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *name;
```

## Default Value
`init(name:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let name` として保持し、`init(name:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L174](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L174)
- [_WKTextExtraction.swift#L430](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L430)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
