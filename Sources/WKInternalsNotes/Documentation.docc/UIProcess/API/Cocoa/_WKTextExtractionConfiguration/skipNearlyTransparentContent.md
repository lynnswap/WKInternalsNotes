# ``WKInternalsNotes/_WKTextExtractionConfiguration/skipNearlyTransparentContent``

透明またはほぼ透明なサブツリーを無視するかを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL skipNearlyTransparentContent;
```

## Default Value
`NO`。

## Discussion
透明度の高いサブツリーを抽出対象から除外する。

## References
- [`_WKTextExtractionInternal.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L41)
- [`_WKTextExtractionInternal.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
