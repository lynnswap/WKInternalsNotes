# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/sourceApplicationSecondaryIdentifier``

送信元アプリの secondary identifier を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *sourceApplicationSecondaryIdentifier WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `sourceApplicationSecondaryIdentifier` の値を返す。

## Discussion
getter は `_configuration->sourceApplicationSecondaryIdentifier()` を `NSString` に変換して返し、setter は `setSourceApplicationSecondaryIdentifier` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L49](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L49)
- [_WKWebsiteDataStoreConfiguration.mm#L305](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L305)
- [_WKWebsiteDataStoreConfiguration.mm#L310](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L310)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
