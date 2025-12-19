# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/disabled``

無効化されているかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isDisabled) BOOL disabled;
```

## Default Value
`init` に渡した `isDisabled` を返す。

## Discussion
`backingIsDisabled` を `@objc(disabled)` の getter で返す。

## References
- [`_WKTextExtractionInternal.h#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L149)
- [`_WKTextExtraction.swift#L174`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L174)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
