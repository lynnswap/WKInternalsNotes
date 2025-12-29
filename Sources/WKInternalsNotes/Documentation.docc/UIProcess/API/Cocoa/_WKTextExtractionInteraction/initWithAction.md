# ``WKInternalsNotes/_WKTextExtractionInteraction/initWithAction(_:)``

アクション種別を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithAction:(_WKTextExtractionAction)action NS_DESIGNATED_INITIALIZER;
```

## Discussion
`action` を保持し、`location` を `CGPointZero` に初期化する。

## References
- [`_WKTextExtraction.mm#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L61)
- [`_WKTextExtraction.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.h#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
