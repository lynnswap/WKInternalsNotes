# ``WKInternalsNotes/WKWebsiteDataStore/_storageSiteValidationEnabled``

ストレージサイト検証の有効状態を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStorageSiteValidationEnabled:) BOOL _storageSiteValidationEnabled WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
初期値は `storageSiteValidationEnabled()` の状態に依存する。

## Discussion
getter は `_websiteDataStore->storageSiteValidationEnabled()` を返し、setter は `setStorageSiteValidationEnabled` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L70)
- [`WKWebsiteDataStore.mm#L848`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L848)
- [`WKWebsiteDataStore.mm#L848`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L848)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
