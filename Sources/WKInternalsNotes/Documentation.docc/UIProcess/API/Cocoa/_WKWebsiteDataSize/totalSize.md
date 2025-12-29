# ``WKInternalsNotes/_WKWebsiteDataSize/totalSize``

合計サイズを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) unsigned long long totalSize;
```

## Default Value
`WebsiteDataRecord::Size::totalSize` の値。

## Discussion
内部の `_size.totalSize` を返す。

## References
- [`_WKWebsiteDataSize.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSize.h#L35)
- [`_WKWebsiteDataSize.mm#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataSize.mm#L43)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
