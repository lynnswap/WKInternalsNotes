# ``WKInternalsNotes/_WKTextExtractionInteraction/action``

抽出操作の種類を表す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKTextExtractionAction action;
```

## Default Value
`initWithAction:` で指定した値。

## Discussion
初期化時に渡された `action` を保持して返す。

## References
- [`_WKTextExtraction.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L61)
- [`_WKTextExtraction.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
