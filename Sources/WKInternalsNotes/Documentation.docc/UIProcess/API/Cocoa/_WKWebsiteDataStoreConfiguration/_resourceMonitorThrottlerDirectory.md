# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_resourceMonitorThrottlerDirectory``

Resource Monitor Throttler の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setResourceMonitorThrottlerDirectory:) NSURL *_resourceMonitorThrottlerDirectory WK_API_AVAILABLE(macos(15.0), ios(18.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `resourceMonitorThrottlerDirectory` の値を返す。

## Discussion
getter は `_configuration->resourceMonitorThrottlerDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setResourceMonitorThrottlerDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L106](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L106)
- [_WKWebsiteDataStoreConfiguration.mm#L583](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L583)
- [_WKWebsiteDataStoreConfiguration.mm#L588](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L588)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
