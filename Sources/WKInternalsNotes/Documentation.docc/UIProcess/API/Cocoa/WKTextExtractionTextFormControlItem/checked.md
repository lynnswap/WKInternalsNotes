# ``WKInternalsNotes/WKTextExtractionTextFormControlItem/checked``

チェック状態かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isChecked) BOOL checked;
```

## Default Value
`init` に渡した `isChecked` を返す。

## Discussion
`backingIsChecked` を `@objc(checked)` の getter で返す。

## References
- [`_WKTextExtractionInternal.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L150)
- [`_WKTextExtraction.swift#L182`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
