# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/websiteDataStore(_:didAllowPrivateTokenUsageByThirdPartyForTesting:forResourceURL:)``

Private Token の third-party 利用許可結果を通知する（テスト用）。

## Objective-C Declaration
```objective-c
- (void)websiteDataStore:(WKWebsiteDataStore *)dataStore didAllowPrivateTokenUsageByThirdPartyForTesting:(BOOL)wasAllowed forResourceURL:(NSURL *)resourceURL;
```

## Discussion
delegate が未実装の場合は呼ばれない。`wasAllowed` と `resourceURL` をそのまま渡す。

## References
- [`_WKWebsiteDataStoreDelegate.h#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L73)
- [`WKWebsiteDataStore.mm#L346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L346)
- [`WKWebsiteDataStore.mm#L351`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L351)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
