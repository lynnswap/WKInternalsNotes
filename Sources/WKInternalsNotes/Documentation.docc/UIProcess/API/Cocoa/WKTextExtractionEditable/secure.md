# ``WKInternalsNotes/WKTextExtractionEditable/secure``

セキュア入力かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isSecure) BOOL secure;
```

## Default Value
`init` に渡した `isSecure` が保持される。

## Discussion
`backingIsSecure` を `@objc(secure)` の getter で返す。

## References
- [`_WKTextExtractionInternal.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L110)
- [`_WKTextExtraction.swift#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
