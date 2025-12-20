# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didReceiveServerRedirectToURL:)``

サーバーリダイレクトを受け取ったことを通知する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didReceiveServerRedirectToURL:(NSURL *)url WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`willSendRequest` でリダイレクト先 URL を `NSURL` に変換して delegate に通知する。

## References
- [`_WKDownloadDelegate.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L39)
- [`LegacyDownloadClient.mm#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L181)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
