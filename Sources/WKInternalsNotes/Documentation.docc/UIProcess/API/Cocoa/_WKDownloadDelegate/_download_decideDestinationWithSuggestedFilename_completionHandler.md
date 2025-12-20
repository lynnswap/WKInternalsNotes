# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:decideDestinationWithSuggestedFilename:completionHandler:)``

ダウンロード先の選択を非同期で決定する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download decideDestinationWithSuggestedFilename:(NSString *)filename completionHandler:(void (^)(BOOL allowOverwrite, NSString *destination))completionHandler;
```

## Discussion
`LegacyDownloadClient` は `didReceiveResponse` を先に通知した後、この completion handler 版を優先して呼び出す。`CompletionHandlerCallChecker` で多重呼び出しを防止する。

## References
- [`_WKDownloadDelegate.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L43)
- [`LegacyDownloadClient.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L140)
- [`LegacyDownloadClient.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
