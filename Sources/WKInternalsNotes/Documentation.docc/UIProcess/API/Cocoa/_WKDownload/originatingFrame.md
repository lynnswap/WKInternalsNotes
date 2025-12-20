# ``WKInternalsNotes/_WKDownload/originatingFrame``

ダウンロード開始元のフレーム情報を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKFrameInfo *originatingFrame WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
内部の `DownloadProxy` が保持する frameInfo を返すため固定の既定値はない。

## Discussion
`DownloadProxy::frameInfo` を `WKFrameInfo` にラップして返す。

## References
- [`_WKDownload.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.h#L46)
- [`_WKDownload.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L113)
- [`_WKDownload.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDownload.mm#L115)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
