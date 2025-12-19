# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:decideDestinationWithSuggestedFilename:allowOverwrite:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (NSString *)_download:(_WKDownload *)download decideDestinationWithSuggestedFilename:(NSString *)filename allowOverwrite:(BOOL *)allowOverwrite WK_API_DEPRECATED_WITH_REPLACEMENT("_download:decideDestinationWithSuggestedFilename:completionHandler:", macos(10.10, 10.13.4), ios(8.0, 11.3));
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKDownloadDelegate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L37)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
