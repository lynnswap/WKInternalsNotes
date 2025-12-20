# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didReceiveResponse:)``

レスポンス受信を通知する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didReceiveResponse:(NSURLResponse *)response;
```

## Discussion
`ResourceResponse` を `NSURLResponse` に変換して delegate に通知する。宛先選択フローでも `decideDestinationWithSuggestedFilename` の先頭で呼び出される。

## References
- [`_WKDownloadDelegate.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L40)
- [`LegacyDownloadClient.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L80)
- [`LegacyDownloadClient.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
