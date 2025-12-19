# ``WKInternalsNotes/WKWebsiteDataStore/_loadedSubresourceDomainsFor(_:completionHandler:)``

読み込み済みサブリソースのドメイン一覧を取得する。

## Objective-C Declaration
```objective-c
- (void)_loadedSubresourceDomainsFor:(WKWebView *)webView completionHandler:(void (^)(NSArray<NSString *> *domains))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`WKWebView` から `page` を取得して `getLoadedSubresourceDomains` を呼び、文字列配列に変換する。`webView`/`page` が無い場合は `nil` を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L75)
- [`WKWebsiteDataStore.mm#L970`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L970)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
