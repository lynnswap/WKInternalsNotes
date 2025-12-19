# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/serviceWorkerProcessTerminationDelayEnabled``

Service Worker プロセス終了遅延を有効にするかを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL serviceWorkerProcessTerminationDelayEnabled WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `serviceWorkerProcessTerminationDelayEnabled` の値を返す。

## Discussion
getter は `_configuration->serviceWorkerProcessTerminationDelayEnabled()` を返し、setter は `_configuration->setServiceWorkerProcessTerminationDelayEnabled` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L82](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L82)
- [_WKWebsiteDataStoreConfiguration.mm#L285](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L285)
- [_WKWebsiteDataStoreConfiguration.mm#L290](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
