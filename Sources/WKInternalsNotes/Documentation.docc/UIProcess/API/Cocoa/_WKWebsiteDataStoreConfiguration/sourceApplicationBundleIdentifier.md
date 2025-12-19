# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/sourceApplicationBundleIdentifier``

送信元アプリの bundle identifier を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *sourceApplicationBundleIdentifier WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `sourceApplicationBundleIdentifier` の値を返す。

## Discussion
getter は `_configuration->sourceApplicationBundleIdentifier()` を `NSString` に変換して返し、setter は `setSourceApplicationBundleIdentifier` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L48](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L48)
- [_WKWebsiteDataStoreConfiguration.mm#L300](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L300)
- [_WKWebsiteDataStoreConfiguration.mm#L295](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L295)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
