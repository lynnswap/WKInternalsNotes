# ``WKInternalsNotes/_WKDownloadDelegate/_downloadDidCancel(_:)``

ダウンロードキャンセルを通知する。

## Objective-C Declaration
```objective-c
- (void)_downloadDidCancel:(_WKDownload *)download;
```

## Discussion
`legacyDidCancel` で `_WKDownload` を生成して通知する。

## References
- [`_WKDownloadDelegate.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L46)
- [`LegacyDownloadClient.mm#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L175)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
