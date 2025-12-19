# ``WKInternalsNotes/WKTextExtractionLinkItem/target``

リンクターゲット文字列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *target;
```

## Default Value
`init(target:...)` の引数値がそのまま保持される。

## Discussion
Swift 実装では `let target` として保持し、`init(target:...)` で設定される。

## References
- [_WKTextExtractionInternal.h#L130](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L130)
- [_WKTextExtraction.swift#L265](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L265)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
