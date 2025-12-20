# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didCreateDestination:)``

ダウンロード先が作成されたことを通知する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didCreateDestination:(NSString *)destination WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`LegacyDownloadClient::didCreateDestination` でパス文字列を渡す。

## References
- [`_WKDownloadDelegate.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L48)
- [`LegacyDownloadClient.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
