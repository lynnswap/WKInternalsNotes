# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/standaloneApplicationURL``

スタンドアロンアプリの URL を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *standaloneApplicationURL WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `standaloneApplicationURL` の値を返す。

## Discussion
getter は `_configuration->standaloneApplicationURL()` を `NSURL` に変換して返し、setter は `setStandaloneApplicationURL` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L99](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L99)
- [_WKWebsiteDataStoreConfiguration.mm#L766](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L766)
- [_WKWebsiteDataStoreConfiguration.mm#L771](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L771)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
