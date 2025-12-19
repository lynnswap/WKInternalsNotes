# ``WKInternalsNotes/WKWebsiteDataStore/_setResourceLoadStatisticsTestingCallback(_:)``

リソースロード統計のテスト用コールバックを設定する。

## Objective-C Declaration
```objective-c
- (void)_setResourceLoadStatisticsTestingCallback:(nullable void (^)(WKWebsiteDataStore *, NSString *))callback WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
永続ストアでのみ `setStatisticsTestingCallback` を設定し、`nil` 指定時は解除する。

## References
- [`WKWebsiteDataStorePrivate.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L74)
- [`WKWebsiteDataStore.mm#L925`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L925)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
