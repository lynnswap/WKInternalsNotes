# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:domain:didOpenDomainViaWindowOpen:withProperty:directly:)``

window.open 由来の window proxy アクセスを通知する。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore domain:(NSString *)registrableDomain didOpenDomainViaWindowOpen:(NSString *)openedRegistrableDomain withProperty:(WKWindowProxyProperty)property directly:(BOOL)directly;
```

## Discussion
delegate が未実装の場合は呼ばれない。`WebCore::WindowProxyProperty` を `WKWindowProxyProperty` に変換し、`PostMessage` と `Closed` 以外は `Other` にまとめて通知する（`InitialOpen` も `Other` 扱い）。

## References
- [`_WKWebsiteDataStoreDelegate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L72)
- [`WKWebsiteDataStore.mm#L326`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L326)
- [`WKWebsiteDataStore.mm#L343`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L343)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
