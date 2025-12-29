# ``WKInternalsNotes/_WKProcessPoolConfiguration/diskCacheSpeculativeValidationEnabled``

ディスクキャッシュの推測的検証を返すが、現在は常に `NO`。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL diskCacheSpeculativeValidationEnabled WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.networkCacheSpeculativeValidationEnabled", macos(10.12, 10.15.4), ios(10.0, 13.4));
```

## Default Value
常に `NO` を返す。

## Discussion
getter は `NO`、setter は空実装のため値を保持しない（deprecated）。

## References
- [`_WKProcessPoolConfiguration.mm#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L101)
- [`_WKProcessPoolConfiguration.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKProcessPoolConfiguration.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
