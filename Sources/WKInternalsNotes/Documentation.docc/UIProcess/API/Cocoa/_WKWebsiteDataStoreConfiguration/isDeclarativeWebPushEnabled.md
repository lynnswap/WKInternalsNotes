# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/isDeclarativeWebPushEnabled``

Declarative Web Push を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL isDeclarativeWebPushEnabled WK_API_AVAILABLE(macos(14.4), ios(17.4), visionos(1.1));
```

## Default Value
`ENABLE(DECLARATIVE_WEB_PUSH)` が無効な場合は常に `NO`。

## Discussion
getter は `ENABLE(DECLARATIVE_WEB_PUSH)` が有効な場合に `_configuration->isDeclarativeWebPushEnabled()` を返し、無効な場合は `NO` を返す。setter は機能有効時のみ `_configuration->setIsDeclarativeWebPushEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L104](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L104)
- [_WKWebsiteDataStoreConfiguration.mm#L619](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L619)
- [_WKWebsiteDataStoreConfiguration.mm#L628](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L628)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
