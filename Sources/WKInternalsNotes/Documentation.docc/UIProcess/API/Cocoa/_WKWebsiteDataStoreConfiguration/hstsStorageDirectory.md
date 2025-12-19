# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/hstsStorageDirectory``

HSTS ストレージの保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=setHSTSStorageDirectory:) NSURL *hstsStorageDirectory WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `hstsStorageDirectory` の値を返す。

## Discussion
getter は `_configuration->hstsStorageDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setHSTSStorageDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L92](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L92)
- [_WKWebsiteDataStoreConfiguration.mm#L367](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L367)
- [_WKWebsiteDataStoreConfiguration.mm#L372](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L372)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
