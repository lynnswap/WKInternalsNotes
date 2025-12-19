# ``WKInternalsNotes/WKWebsiteDataStore/_synthesizeAppIsBackground(_:)``

アプリのバックグラウンド状態を合成して通知する。

## Objective-C Declaration
```objective-c
- (void)_synthesizeAppIsBackground:(BOOL)background WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`NetworkProcess` の `synthesizeAppIsBackground` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L121)
- [`WKWebsiteDataStore.mm#L1221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1221)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
