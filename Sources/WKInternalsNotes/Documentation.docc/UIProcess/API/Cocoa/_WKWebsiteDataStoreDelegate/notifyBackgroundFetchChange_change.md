# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/notifyBackgroundFetchChange(_:change:)``

Background Fetch の状態変化を通知する。

## Objective-C Declaration
```objective-c
- (void)notifyBackgroundFetchChange:(NSString *)backgroundFetchIdentifier change:(WKBackgroundFetchChange)change;
```

## Discussion
delegate が未実装の場合は呼ばれない。内部の `BackgroundFetchChange` を `WKBackgroundFetchChange` に変換して通知する。

## References
- [`_WKWebsiteDataStoreDelegate.h#L71`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L71)
- [`WKWebsiteDataStore.mm#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L306)
- [`WKWebsiteDataStore.mm#L323`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L323)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
