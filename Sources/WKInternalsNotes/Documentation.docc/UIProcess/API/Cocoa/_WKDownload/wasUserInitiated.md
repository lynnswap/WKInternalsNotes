# ``WKInternalsNotes/_WKDownload/wasUserInitiated``

ユーザー操作によって開始されたかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL wasUserInitiated WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
内部の `DownloadProxy` が保持する状態に依存する。

## Discussion
`DownloadProxy::wasUserInitiated` をそのまま返す。

## References
- [`_WKDownload.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L44)
- [`_WKDownload.mm#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L103)
- [`_WKDownload.mm#L105`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L105)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
