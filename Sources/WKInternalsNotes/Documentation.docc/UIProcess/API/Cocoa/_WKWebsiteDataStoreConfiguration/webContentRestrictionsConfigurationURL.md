# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/webContentRestrictionsConfigurationURL``

WebContentRestrictions の設定ファイル URL を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *webContentRestrictionsConfigurationURL WK_API_AVAILABLE(macos(26.0), ios(26.0));
```

## Default Value
`WEBCONTENTRESTRICTIONS_PATH_SPI` が無効、または未設定の場合は `nil`。

## Discussion
getter は `WEBCONTENTRESTRICTIONS_PATH_SPI` が有効な場合のみ `_configuration->webContentRestrictionsConfigurationFile()` を確認し、空でなければ file URL を返す。setter は `checkURLArgument` で検証し、機能有効時のみ設定する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L107](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L107)
- [_WKWebsiteDataStoreConfiguration.mm#L600](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L600)
- [_WKWebsiteDataStoreConfiguration.mm#L611](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L611)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
