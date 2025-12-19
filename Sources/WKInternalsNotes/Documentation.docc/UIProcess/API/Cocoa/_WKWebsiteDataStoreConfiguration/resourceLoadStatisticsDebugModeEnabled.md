# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/resourceLoadStatisticsDebugModeEnabled``

Resource Load Statistics のデバッグモードを有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL resourceLoadStatisticsDebugModeEnabled WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `resourceLoadStatisticsDebugModeEnabled` の値を返す。

## Discussion
getter は `_configuration->resourceLoadStatisticsDebugModeEnabled()` を返し、setter は `_configuration->setResourceLoadStatisticsDebugModeEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L68](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L68)
- [_WKWebsiteDataStoreConfiguration.mm#L826](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L826)
- [_WKWebsiteDataStoreConfiguration.mm#L831](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L831)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
