# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/webPushPartitionString``

Web Push のパーティション文字列を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setWebPushPartitionString:) NSString *webPushPartitionString WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `webPushPartitionString` の値を返す。

## Discussion
getter は `_configuration->webPushPartitionString()` を `NSString` に変換して返し、setter は `_configuration->setWebPushPartitionString` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L101](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L101)
- [_WKWebsiteDataStoreConfiguration.mm#L455](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L455)
- [_WKWebsiteDataStoreConfiguration.mm#L460](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L460)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
