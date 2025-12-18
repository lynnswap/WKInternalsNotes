# ``WKInternalsNotes/WKDownloadDelegatePrivate/_download(_:decidePlaceholderPolicy:)``

プレースホルダーファイル作成の可否を決めるために呼ばれる。

## Objective-C Declaration
```objective-c
- (void)_download:(WKDownload *)download decidePlaceholderPolicy:(void (^)(_WKPlaceholderPolicy, NSURL *))completionHandler WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
`WKDownload` は delegate が `_download:decidePlaceholderPolicy:` に応答する場合はそれを呼び、未実装の場合は公開 API の `download:decidePlaceholderPolicy:` を呼ぶ。どちらにも応答しない場合は `UseDownloadPlaceholder::No` で継続する。返された `_WKPlaceholderPolicy` は `UseDownloadPlaceholder` に変換され、無効値は `NSInvalidArgumentException` を投げる。

## References
- [`WKDownloadDelegatePrivate.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownloadDelegatePrivate.h#L57)
- [`WKDownload.mm#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownload.mm#L148)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
