# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/suppressesConnectionTerminationOnSystemChange``

システム変更時の接続終了抑止を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL suppressesConnectionTerminationOnSystemChange WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `suppressesConnectionTerminationOnSystemChange` の値を返す。

## Discussion
getter は `_configuration->suppressesConnectionTerminationOnSystemChange()` を返し、setter は `_configuration->setSuppressesConnectionTerminationOnSystemChange` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L90](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L90)
- [_WKWebsiteDataStoreConfiguration.mm#L646](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L646)
- [_WKWebsiteDataStoreConfiguration.mm#L651](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L651)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
