# ``WKInternalsNotes/WKDownloadDelegatePrivate/_download(_:didReceiveFinalURL:)``

最終的なダウンロード保存先 URL を受け取ったタイミングで通知される。

## Objective-C Declaration
```objective-c
- (void)_download:(WKDownload *)download didReceiveFinalURL:(NSURL *)url WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
`HAVE(MODERN_DOWNLOADPROGRESS)` の場合に呼ばれ、delegate が未設定または未実装なら何もしない。ブックマークデータから URL を復元し、失敗時はログを出して `url` にフォールバックする。private 版の実装があれば `_download:didReceiveFinalURL:` を呼び、なければ公開 API の `download:didReceiveFinalURL:` を呼ぶ。

## References
- [`WKDownloadDelegatePrivate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownloadDelegatePrivate.h#L71)
- [`WKDownload.mm#L246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownload.mm#L246)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
