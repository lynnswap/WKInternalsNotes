# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/boundInterfaceIdentifier``

バインドするネットワークインターフェイス識別子を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSString *boundInterfaceIdentifier WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `boundInterfaceIdentifier` の値を返す。

## Discussion
getter は `_configuration->boundInterfaceIdentifier()` を `NSString` に変換して返し、setter は `_configuration->setBoundInterfaceIdentifier` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L59](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L59)
- [_WKWebsiteDataStoreConfiguration.mm#L666](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L666)
- [_WKWebsiteDataStoreConfiguration.mm#L671](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L671)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
