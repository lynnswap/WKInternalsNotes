# ``WKInternalsNotes/_WKDownloadDelegate/_download(_:shouldDecodeSourceDataOfMIMEType:)``

ソースデータをデコードするかどうかを問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_download:(_WKDownload *)download shouldDecodeSourceDataOfMIMEType:(NSString *)MIMEType WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Discussion
`LegacyDownloadClient` は selector の有無をチェックするだけで、UIProcess/Cocoa からの呼び出し箇所は見当たらない。

## References
- [`_WKDownloadDelegate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownloadDelegate.h#L50)
- [`LegacyDownloadClient.mm#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/LegacyDownloadClient.mm#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
