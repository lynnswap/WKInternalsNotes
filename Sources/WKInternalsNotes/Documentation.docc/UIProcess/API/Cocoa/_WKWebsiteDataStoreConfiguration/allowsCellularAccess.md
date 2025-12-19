# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/allowsCellularAccess``

セルラーアクセスを許可するかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL allowsCellularAccess WK_API_AVAILABLE(macos(10.15.4), ios(14.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `allowsCellularAccess` の値を返す。

## Discussion
getter は `_configuration->allowsCellularAccess()` を返し、setter は `_configuration->setAllowsCellularAccess` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L60](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L60)
- [_WKWebsiteDataStoreConfiguration.mm#L676](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L676)
- [_WKWebsiteDataStoreConfiguration.mm#L681](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L681)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
