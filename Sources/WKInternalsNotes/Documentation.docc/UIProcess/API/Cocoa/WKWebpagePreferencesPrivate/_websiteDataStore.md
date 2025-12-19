# ``WKInternalsNotes/WKWebpagePreferences/_websiteDataStore``

ページに適用する WebsiteDataStore を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, strong, setter=_setWebsiteDataStore:) WKWebsiteDataStore *_websiteDataStore;
```

## Default Value
初期値は `WebsitePolicies::websiteDataStore()` に依存する。

## Discussion
getter は `websiteDataStore()` をラップして返す。setter は `WKWebsiteDataStore` の内部 `_websiteDataStore` を渡して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L104)
- [`WKWebpagePreferences.mm#L412`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L412)
- [`WKWebpagePreferences.mm#L417`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L417)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
