# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_serviceWorkerRegistrationDirectory``

Service Worker 登録情報の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setServiceWorkerRegistrationDirectory:) NSURL *_serviceWorkerRegistrationDirectory WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `serviceWorkerRegistrationDirectory` の値を返す。

## Discussion
getter は `_configuration->serviceWorkerRegistrationDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setServiceWorkerRegistrationDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L81](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L81)
- [_WKWebsiteDataStoreConfiguration.mm#L268](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L268)
- [_WKWebsiteDataStoreConfiguration.mm#L273](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L273)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
