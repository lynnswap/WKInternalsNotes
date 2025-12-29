# ``WKInternalsNotes/_WKTextExtractionInteraction/nodeIdentifier``

対象ノードの識別子を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSString *nodeIdentifier;
```

## Default Value
`nil`。

## Discussion
setter は `copy` した値を保持し、getter は保持している文字列を返す。

## References
- [`_WKTextExtraction.mm#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L71)
- [`_WKTextExtraction.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L76)
- [`_WKTextExtraction.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L83)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
