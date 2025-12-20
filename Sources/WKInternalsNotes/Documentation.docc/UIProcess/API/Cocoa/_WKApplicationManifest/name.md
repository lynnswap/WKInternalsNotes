# ``WKInternalsNotes/_WKApplicationManifest/name``

アプリケーション名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSString *name;
```

## Discussion
`ApplicationManifest` の `name` を `NSString` に変換して返す（`null` の場合は `nil`）。

## References
- [`_WKApplicationManifest.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L77)
- [`_WKApplicationManifest.mm#L388`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L388)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
