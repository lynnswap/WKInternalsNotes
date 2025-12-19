# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/unifiedOriginStorageLevel``

Unified Origin Storage Level を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) _WKUnifiedOriginStorageLevel unifiedOriginStorageLevel WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`_configuration->unifiedOriginStorageLevel()` を対応する enum に変換して返す。

## Discussion
getter は `WebKit::UnifiedOriginStorageLevel` を `_WKUnifiedOriginStorageLevel` に変換して返す。setter は逆変換した上で `_configuration->setUnifiedOriginStorageLevel` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L102](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L102)
- [_WKWebsiteDataStoreConfiguration.mm#L445](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L445)
- [_WKWebsiteDataStoreConfiguration.mm#L450](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L450)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
