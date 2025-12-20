# ``WKInternalsNotes/_WKApplicationManifest/shortName``

短縮名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSString *shortName;
```

## Discussion
`ApplicationManifest` の `shortName` を `NSString` に変換して返す（`null` の場合は `nil`）。

## References
- [`_WKApplicationManifest.h#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L78)
- [`_WKApplicationManifest.mm#L393`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L393)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
