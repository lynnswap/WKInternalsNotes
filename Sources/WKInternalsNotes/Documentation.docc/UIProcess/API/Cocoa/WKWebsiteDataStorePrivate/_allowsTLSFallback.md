# ``WKInternalsNotes/WKWebsiteDataStore/_allowsTLSFallback``

TLS フォールバックの可否を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowsTLSFallback:) BOOL _allowsTLSFallback WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`NO`。

## Discussion
getter は `NO` を返し、setter は空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L69)
- [`WKWebsiteDataStore.mm#L911`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L911)
- [`WKWebsiteDataStore.mm#L915`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L915)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
