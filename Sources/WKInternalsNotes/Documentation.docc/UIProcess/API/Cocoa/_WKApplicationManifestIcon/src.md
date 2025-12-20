# ``WKInternalsNotes/_WKApplicationManifestIcon/src``

アイコンの URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *src;
```

## Discussion
`initWithCoreIcon:` で `icon->src` を `NSURL` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L109)
- [`_WKApplicationManifest.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L116)
- [`_WKApplicationManifest.mm#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L141)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
