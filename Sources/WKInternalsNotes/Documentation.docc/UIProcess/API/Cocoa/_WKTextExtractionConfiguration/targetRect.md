# ``WKInternalsNotes/_WKTextExtractionConfiguration/targetRect``

抽出対象の矩形を指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGRect targetRect;
```

## Default Value
`CGRectNull`（全要素を対象）。

## Discussion
指定した矩形と交差する要素のみを抽出対象にする。`init` では `CGRectNull` を設定する。

## References
- [`_WKTextExtraction.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L37)
- [`_WKTextExtraction.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L42)
- [`_WKTextExtraction.mm#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L40)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
