# ``WKInternalsNotes/_WKProcessPoolConfiguration/diskCacheSizeOverride``

ディスクキャッシュサイズの上書きを返すが、現在は常に 0。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSInteger diskCacheSizeOverride WK_API_DEPRECATED("Use [WKWebsiteDataStore nonPersistentDataStore] to limit disk cache size to 0", macos(10.11, 10.14.4), ios(9.0, 12.2));
```

## Default Value
常に `0` を返す。

## Discussion
getter は 0 を返し、setter は空実装のため値を保持しない（deprecated）。

## References
- [`_WKProcessPoolConfiguration.mm#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L92)
- [`_WKProcessPoolConfiguration.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L97)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
