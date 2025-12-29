# ``WKInternalsNotes/_WKTextExtractionInteraction/location``

操作位置を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) CGPoint location;
```

## Default Value
`CGPointZero`。

## Discussion
`initWithAction:` で `CGPointZero` に初期化し、setter で `hasSetLocation` を `YES` にして位置を更新する。

## References
- [`_WKTextExtraction.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L61)
- [`_WKTextExtraction.mm#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L91)
- [`_WKTextExtraction.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L88)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
