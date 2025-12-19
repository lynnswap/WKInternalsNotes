# ``WKInternalsNotes/WKTextExtractionLink/url``

リンク先 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSURL *url;
```

## Default Value
`init(url:range:)` の引数値が `backingURL` に保持される。

## Discussion
`@_objcImplementation` の制約回避のため `backingURL` に保持し、`URL` として返す。

## References
- [_WKTextExtractionInternal.h#L102](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L102)
- [_WKTextExtraction.swift#L307](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.swift#L307)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
