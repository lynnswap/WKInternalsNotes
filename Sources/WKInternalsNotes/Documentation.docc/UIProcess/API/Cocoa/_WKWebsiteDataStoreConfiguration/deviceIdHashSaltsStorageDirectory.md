# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/deviceIdHashSaltsStorageDirectory``

Device ID hash salts の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *deviceIdHashSaltsStorageDirectory WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `deviceIdHashSaltsStorageDirectory` の値を返す。

## Discussion
getter は `_configuration->deviceIdHashSaltsStorageDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setDeviceIdHashSaltsStorageDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L84](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L84)
- [_WKWebsiteDataStoreConfiguration.mm#L160](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L160)
- [_WKWebsiteDataStoreConfiguration.mm#L165](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L165)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
