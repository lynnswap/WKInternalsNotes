# ``WKInternalsNotes/WKWebsiteDataStore/_resourceLoadStatisticsEnabled``

リソースロード統計の有効状態を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setResourceLoadStatisticsEnabled:) BOOL _resourceLoadStatisticsEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
初期値は `trackingPreventionEnabled()` の状態に依存する。

## Discussion
getter は `trackingPreventionEnabled()` を返し、setter は `setTrackingPreventionEnabled` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L62)
- [`WKWebsiteDataStore.mm#L823`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L823)
- [`WKWebsiteDataStore.mm#L828`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L828)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
