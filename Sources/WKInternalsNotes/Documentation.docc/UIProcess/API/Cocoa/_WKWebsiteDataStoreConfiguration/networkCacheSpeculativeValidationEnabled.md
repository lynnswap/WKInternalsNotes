# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/networkCacheSpeculativeValidationEnabled``

Network Cache の speculative validation を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL networkCacheSpeculativeValidationEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `networkCacheSpeculativeValidationEnabled` の値を返す。

## Discussion
getter は `_configuration->networkCacheSpeculativeValidationEnabled()` を返し、setter は `_configuration->setNetworkCacheSpeculativeValidationEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L53](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L53)
- [_WKWebsiteDataStoreConfiguration.mm#L475](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L475)
- [_WKWebsiteDataStoreConfiguration.mm#L480](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L480)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
