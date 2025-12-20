# ``WKInternalsNotes/_WKApplicationManifestIcon/type``

アイコンの MIME type を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSString *type;
```

## Discussion
`initWithCoreIcon:` で `icon->type` を `NSString` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L111)
- [`_WKApplicationManifest.mm#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L126)
- [`_WKApplicationManifest.mm#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
