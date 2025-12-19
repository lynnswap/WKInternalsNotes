# ``WKInternalsNotes/WKWebsiteDataStore/_clearLoadedSubresourceDomainsFor(_:)``

指定 WebView のロード済みサブリソースドメインをクリアする。

## Objective-C Declaration
```objective-c
- (void)_clearLoadedSubresourceDomainsFor:(WKWebView *)webView WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`webView` が `nil` の場合は何もしない。`[webView _page]` が存在すれば `clearLoadedSubresourceDomains()` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L76)
- [`WKWebsiteDataStore.mm#L991`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L991)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
