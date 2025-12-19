# ``WKInternalsNotes/WKWebsiteDataStore/_hasServiceWorkerBackgroundActivityForTesting()``

テスト用に Service Worker のバックグラウンド活動有無を返す。

## Objective-C Declaration
```objective-c
-(bool)_hasServiceWorkerBackgroundActivityForTesting WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`hasServiceWorkerBackgroundActivityForTesting()` の結果を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L128)
- [`WKWebsiteDataStore.mm#L1264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1264)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
