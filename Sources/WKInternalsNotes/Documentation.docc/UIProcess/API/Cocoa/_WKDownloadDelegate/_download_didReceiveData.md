# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didReceiveData:)``

受信データ量を通知する（旧 API）。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didReceiveData:(uint64_t)length;
```

## Discussion
`didWriteData:totalBytesWritten:totalBytesExpectedToWrite:` を実装していない場合にのみ呼ばれる。

## References
- [`_WKDownloadDelegate.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L41)
- [`LegacyDownloadClient.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
