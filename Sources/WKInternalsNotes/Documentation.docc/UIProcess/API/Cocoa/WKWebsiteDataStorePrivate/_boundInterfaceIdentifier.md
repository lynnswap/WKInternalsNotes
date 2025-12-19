# ``WKInternalsNotes/WKWebsiteDataStore/_boundInterfaceIdentifier``

通信に使用するインターフェース識別子を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setBoundInterfaceIdentifier:) NSString *_boundInterfaceIdentifier WK_API_DEPRECATED_WITH_REPLACEMENT("_WKWebsiteDataStoreConfiguration.boundInterfaceIdentifier", macos(10.13.4, 10.15.4), ios(11.3, 13.4));
```

## Default Value
`nil`。

## Discussion
getter は `nil` を返し、setter は空実装。

## References
- [`WKWebsiteDataStorePrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L66)
- [`WKWebsiteDataStore.mm#L893`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L893)
- [`WKWebsiteDataStore.mm#L893`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L893)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
