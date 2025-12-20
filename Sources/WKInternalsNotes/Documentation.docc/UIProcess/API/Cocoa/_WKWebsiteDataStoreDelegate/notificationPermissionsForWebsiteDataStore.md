# ``WKInternalsNotes/_WKWebsiteDataStoreDelegate/notificationPermissionsForWebsiteDataStore(_:)``

通知許可の一覧を返す。

## Objective-C Declaration
```objective-c
- (NSDictionary<NSString *, NSNumber *> *)notificationPermissionsForWebsiteDataStore:(WKWebsiteDataStore *)dataStore;
```

## Discussion
delegate が未設定または未実装の場合は空の map を返す。返却された辞書のキーは URL 文字列として解釈され、`SecurityOriginData` に変換できない場合はログを出してスキップする。値は `bool` として扱われる。

## References
- [`_WKWebsiteDataStoreDelegate.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreDelegate.h#L65)
- [`WKWebsiteDataStore.mm#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L217)
- [`WKWebsiteDataStore.mm#L229`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L229)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
