# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:decideDestinationWithSuggestedFilename:allowOverwrite:)``

ダウンロード先を同期的に決定する（deprecated）。

## Objective-C Declaration
```objective-c
- (NSString *)_download:(_WKDownload *)download decideDestinationWithSuggestedFilename:(NSString *)filename allowOverwrite:(BOOL *)allowOverwrite WK_API_DEPRECATED_WITH_REPLACEMENT("_download:decideDestinationWithSuggestedFilename:completionHandler:", macos(10.10, 10.13.4), ios(8.0, 11.3));
```

## Discussion
`LegacyDownloadClient` はこの旧 API を優先的に呼び出し、`allowOverwrite` と返却されたパスを completion handler に変換して渡す。

## References
- [`_WKDownloadDelegate.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L52)
- [`LegacyDownloadClient.mm#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L147)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
