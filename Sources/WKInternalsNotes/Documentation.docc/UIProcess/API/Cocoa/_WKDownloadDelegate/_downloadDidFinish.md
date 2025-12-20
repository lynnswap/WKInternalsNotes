# ``WKInternalsNotes/_WKDownloadDelegate/_downloadDidFinish(_:)``

ダウンロード完了を通知する。

## Objective-C Declaration
```objective-c
- (void)_downloadDidFinish:(_WKDownload *)download;
```

## Discussion
`LegacyDownloadClient::didFinish` で `_WKDownload` を生成して通知する。

## References
- [`_WKDownloadDelegate.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L44)
- [`LegacyDownloadClient.mm#L163`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L163)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
