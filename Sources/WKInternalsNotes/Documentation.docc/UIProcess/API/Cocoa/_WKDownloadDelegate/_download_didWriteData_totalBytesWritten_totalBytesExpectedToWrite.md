# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:)``

書き込み済みバイト数の詳細を通知する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didWriteData:(uint64_t)bytesWritten totalBytesWritten:(uint64_t)totalBytesWritten totalBytesExpectedToWrite:(uint64_t)totalBytesExpectedToWrite WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`LegacyDownloadClient::didReceiveData` で優先的に呼び出され、`didReceiveData:` より新しい詳細通知として扱われる。

## References
- [`_WKDownloadDelegate.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L42)
- [`LegacyDownloadClient.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
