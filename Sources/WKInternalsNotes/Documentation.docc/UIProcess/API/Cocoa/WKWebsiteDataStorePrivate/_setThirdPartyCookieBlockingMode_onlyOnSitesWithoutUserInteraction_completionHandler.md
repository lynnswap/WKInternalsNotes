# ``WKInternalsNotes/WKWebsiteDataStore/_setThirdPartyCookieBlockingMode(_:onlyOnSitesWithoutUserInteraction:completionHandler:)``

テスト用に第三者 Cookie ブロックモードを設定する。

## Objective-C Declaration
```objective-c
- (void)_setThirdPartyCookieBlockingMode:(BOOL)enabled onlyOnSitesWithoutUserInteraction:(BOOL)onlyOnSitesWithoutUserInteraction completionHandler:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
引数に応じて `ThirdPartyCookieBlockingMode` を選び、`setResourceLoadStatisticsShouldBlockThirdPartyCookiesForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L91)
- [`WKWebsiteDataStore.mm#L1091`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1091)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
