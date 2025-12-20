# ``WKInternalsNotes/_WKApplicationManifest/startURL``

起動 URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSURL *startURL;
```

## Discussion
`ApplicationManifest` の `startURL` を `NSURL` に変換して返す。

## References
- [`_WKApplicationManifest.h#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.h#L83)
- [`_WKApplicationManifest.mm#L418`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKApplicationManifest.mm#L418)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
