# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/enableInAppBrowserPrivacyForTesting``

テスト用に In-App Browser Privacy を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL enableInAppBrowserPrivacyForTesting WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `enableInAppBrowserPrivacyForTesting` の値を返す。

## Discussion
getter は `_configuration->enableInAppBrowserPrivacyForTesting()` を返し、setter は `_configuration->setEnableInAppBrowserPrivacyForTesting` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L93](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L93)
- [_WKWebsiteDataStoreConfiguration.mm#L776](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L776)
- [_WKWebsiteDataStoreConfiguration.mm#L781](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L781)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
