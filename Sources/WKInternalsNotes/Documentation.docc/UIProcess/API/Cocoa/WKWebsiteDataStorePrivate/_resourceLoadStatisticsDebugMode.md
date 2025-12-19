# ``WKInternalsNotes/WKWebsiteDataStore/_resourceLoadStatisticsDebugMode``

リソースロード統計のデバッグモードを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setResourceLoadStatisticsDebugMode:) BOOL _resourceLoadStatisticsDebugMode WK_API_AVAILABLE(macos(10.14), ios(12.0));
```

## Default Value
初期値は `resourceLoadStatisticsDebugMode()` の状態に依存する。

## Discussion
getter は `resourceLoadStatisticsDebugMode()` を返し、setter は `setResourceLoadStatisticsDebugMode` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L63`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L63)
- [`WKWebsiteDataStore.mm#L833`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L833)
- [`WKWebsiteDataStore.mm#L833`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L833)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
