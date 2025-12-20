# ``WKInternalsNotes/_WKApplicationManifestIcon/purposes``

アイコン用途の配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSArray<NSNumber *> *purposes;
```

## Discussion
`initWithCoreIcon:` で `icon->purposes` を `NSArray<NSNumber *>` に変換して保持し、そのまま返す。

## References
- [`_WKApplicationManifest.h#L112`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L112)
- [`_WKApplicationManifest.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L127)
- [`_WKApplicationManifest.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
