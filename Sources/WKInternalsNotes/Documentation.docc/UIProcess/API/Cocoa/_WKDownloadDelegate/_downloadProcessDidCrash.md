# ``WKInternalsNotes/_WKDownloadDelegate/_downloadProcessDidCrash(_:)``

ダウンロードプロセスのクラッシュを通知する。

## Objective-C Declaration
```objective-c
- (void)_downloadProcessDidCrash:(_WKDownload *)download WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`LegacyDownloadClient::processDidCrash` で `_WKDownload` を生成して通知する。

## References
- [`_WKDownloadDelegate.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L49)
- [`LegacyDownloadClient.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L134)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
