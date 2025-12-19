# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/readonly``

読み取り専用かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isReadonly) BOOL readonly;
```

## Default Value
`init` に渡した `isReadonly` を返す。

## Discussion
`backingIsReadonly` を `@objc(readonly)` の getter で返す。

## References
- [`_WKTextExtractionInternal.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L62)
- [`_WKTextExtraction.swift#L166`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L166)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
