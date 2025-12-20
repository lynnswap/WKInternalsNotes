# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didFailWithError:)``

ダウンロード失敗を通知する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didFailWithError:(NSError *)error;
```

## Discussion
`ResourceError` を `NSError` に変換して delegate に渡す。

## References
- [`_WKDownloadDelegate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L45)
- [`LegacyDownloadClient.mm#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
