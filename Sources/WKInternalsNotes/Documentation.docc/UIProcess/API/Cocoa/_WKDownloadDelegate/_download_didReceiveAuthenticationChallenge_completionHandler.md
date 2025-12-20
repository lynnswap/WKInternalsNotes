# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:didReceiveAuthenticationChallenge:completionHandler:)``

認証チャレンジを delegate で処理する。

## Objective-C Declaration
```objective-c
- (void)_download:(_WKDownload *)download didReceiveAuthenticationChallenge:(NSURLAuthenticationChallenge *)challenge completionHandler:(void (^)(NSURLSessionAuthChallengeDisposition, NSURLCredential*))completionHandler WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
delegate が未実装の場合は `PerformDefaultHandling` を選択する。実装されている場合は completion handler の戻り値を `AuthenticationChallengeDisposition` に変換して listener に渡す。

## References
- [`_WKDownloadDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L47)
- [`LegacyDownloadClient.mm#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L94)
- [`LegacyDownloadClient.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
