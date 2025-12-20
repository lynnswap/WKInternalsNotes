# ``WKInternalsNotes/_WKDownload/publishProgressAtURL(_:)``

指定した URL へ進捗公開を要求する。

## Objective-C Declaration
```objective-c
- (void)publishProgressAtURL:(NSURL *)URL WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
`DownloadProxy::publishProgress` に URL を渡して進捗公開を依頼する。

## References
- [`_WKDownload.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L39)
- [`_WKDownload.mm#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L80)
- [`_WKDownload.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L82)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
