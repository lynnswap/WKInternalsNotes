# ``WKInternalsNotes/_WKApplicationManifestIcon/sizes``

アイコンサイズの配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<NSString *> *sizes;
```

## Discussion
`initWithCoreIcon:` で `icon->sizes` を `NSArray<NSString *>` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L110)
- [`_WKApplicationManifest.mm#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L121)
- [`_WKApplicationManifest.mm#L146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L146)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
