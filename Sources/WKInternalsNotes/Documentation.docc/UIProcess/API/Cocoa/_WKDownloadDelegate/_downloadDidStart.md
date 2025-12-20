# ``WKInternalsNotes/_WKDownloadDelegate/_downloadDidStart(_:)``

ダウンロード開始時に呼び出される。

## Objective-C Declaration
```objective-c
- (void)_downloadDidStart:(_WKDownload *)download;
```

## Discussion
`LegacyDownloadClient` が `DownloadProxy` から `_WKDownload` を生成して delegate に通知する。

## References
- [`_WKDownloadDelegate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L38)
- [`LegacyDownloadClient.mm#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
