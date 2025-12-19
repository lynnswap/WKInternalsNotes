# ``WKInternalsNotes/WKWebsiteDataStore/_persistedSites``

永続化対象サイトの一覧を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPersistedSites:) NSArray<NSURL *> *_persistedSites WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Default Value
初期値は `persistedSiteURLs()` の内容に依存する。

## Discussion
getter は `persistedSiteURLs()` を `NSURL` 配列へ変換する。setter は配列から有効な URL を集めて `setPersistedSiteURLs` に渡す。

## References
- [`WKWebsiteDataStorePrivate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L71)
- [`WKWebsiteDataStore.mm#L858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L858)
- [`WKWebsiteDataStore.mm#L858`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L858)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
