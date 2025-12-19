# ``WKInternalsNotes/WKTextExtractionLinkItem/url``

リンク先 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSURL *url;
```

## Default Value
`init(url:...)` の引数値が `backingURL` に保持される。

## Discussion
Swift 実装では `backingURL` を保持し、`URL?` にブリッジして返す。

## References
- [_WKTextExtractionInternal.h#L131](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L131)
- [_WKTextExtraction.swift#L269](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L269)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
