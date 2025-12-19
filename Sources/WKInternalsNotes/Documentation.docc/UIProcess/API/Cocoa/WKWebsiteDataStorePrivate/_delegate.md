# ``WKInternalsNotes/WKWebsiteDataStore/_delegate``

`_WKWebsiteDataStoreDelegate` を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nullable, nonatomic, weak) id <_WKWebsiteDataStoreDelegate> _delegate WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
未設定時は `nil`。

## Discussion
getter は `_delegate` を返す。setter は `_delegate` を更新し、`WebsiteDataStoreClient` を設定する。

## References
- [`WKWebsiteDataStorePrivate.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L110)
- [`WKWebsiteDataStore.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L104)
- [`WKWebsiteDataStore.mm#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
