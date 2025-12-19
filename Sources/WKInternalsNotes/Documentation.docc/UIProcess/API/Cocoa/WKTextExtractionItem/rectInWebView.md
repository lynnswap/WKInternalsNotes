# ``WKInternalsNotes/WKTextExtractionItem/rectInWebView``

WebView 座標系の矩形を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) CGRect rectInWebView;
```

## Default Value
`init(with:)` の引数値がそのまま保持される。

## Discussion
Swift の `@_objcImplementation` extension で `let rectInWebView` を保持し、`init(with:)` の引数から設定される。

## References
- [_WKTextExtractionInternal.h#L116](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L116)
- [_WKTextExtraction.swift#L37](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
