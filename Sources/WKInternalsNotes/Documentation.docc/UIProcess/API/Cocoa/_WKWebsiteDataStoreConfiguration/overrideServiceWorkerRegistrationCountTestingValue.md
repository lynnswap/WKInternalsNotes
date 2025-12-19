# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/overrideServiceWorkerRegistrationCountTestingValue``

Service Worker 登録数のテスト用上書き値を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic) NSUInteger overrideServiceWorkerRegistrationCountTestingValue WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
未設定の場合は `0` を返す。

## Discussion
getter は `_configuration->overrideServiceWorkerRegistrationCountTestingValue().value_or(0)` を返し、setter は `_configuration->setOverrideServiceWorkerRegistrationCountTestingValue` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L67](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L67)
- [_WKWebsiteDataStoreConfiguration.mm#L741](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L741)
- [_WKWebsiteDataStoreConfiguration.mm#L746](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L746)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
