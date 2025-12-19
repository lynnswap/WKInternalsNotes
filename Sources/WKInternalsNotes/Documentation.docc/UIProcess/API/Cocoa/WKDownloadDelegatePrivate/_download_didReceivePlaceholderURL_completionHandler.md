# ``WKInternalsNotes/WKDownloadDelegatePrivate/_download(_:didReceivePlaceholderURL:completionHandler:)``

ダウンロード中のプレースホルダー URL を受け取ったタイミングで通知される。

## Objective-C Declaration
```objective-c
- (void)_download:(WKDownload *)download didReceivePlaceholderURL:(NSURL *)url completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
`HAVE(MODERN_DOWNLOADPROGRESS)` の場合に呼ばれ、delegate が未設定または未実装なら `completionHandler` を即時実行して戻る。ブックマークデータから URL を復元し、失敗時はログを出して `url` にフォールバックする。private 版の実装があれば `_download:didReceivePlaceholderURL:completionHandler:` を呼び、なければ公開 API の `download:didReceivePlaceholderURL:completionHandler:` を呼ぶ。

## References
- [`WKDownloadDelegatePrivate.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownloadDelegatePrivate.h#L57)
- [`WKDownload.mm#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKDownload.mm#L51)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
