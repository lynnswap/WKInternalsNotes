# ``WKInternalsNotes/_WKDownload/cancel()``

ダウンロードをキャンセルする。

## Objective-C Declaration
```objective-c
- (void)cancel;
```

## Discussion
`DownloadProxy::cancel` に委譲し、キャンセル完了時に `legacyDidCancel` を呼び出してレガシーのクライアントに通知する。

## References
- [`_WKDownload.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L38)
- [`_WKDownload.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L73)
- [`_WKDownload.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L75)
- [`_WKDownload.mm#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L76)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
