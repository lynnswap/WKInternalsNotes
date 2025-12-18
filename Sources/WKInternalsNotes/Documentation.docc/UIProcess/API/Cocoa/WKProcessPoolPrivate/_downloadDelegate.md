# ``WKInternalsNotes/WKProcessPool/_downloadDelegate``

ダウンロードの legacy delegate を取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak, setter=_setDownloadDelegate:) id <_WKDownloadDelegate> _downloadDelegate WK_API_DEPRECATED_WITH_REPLACEMENT("WKDownload.downloadDelegate", macos(10.10, 12.0), ios(8.0, 15.0));
```

## Default Value
未設定の場合は `nil`。

## Discussion
getter は `_downloadDelegate` を返す。setter は `_downloadDelegate` を更新し、`LegacyDownloadClient` を `WebProcessPool` に登録する。

## References
- [`WKProcessPoolPrivate.h#L98`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h#L98)
- [`WKProcessPool.mm#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L316)
- [`WKProcessPool.mm#L321`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPool.mm#L321)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
