# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_cacheStorageDirectory``

Cache Storage の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCacheStorageDirectory:) NSURL *_cacheStorageDirectory WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `cacheStorageDirectory` の値を返す。

## Discussion
getter は `_configuration->cacheStorageDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setCacheStorageDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L80](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L80)
- [_WKWebsiteDataStoreConfiguration.mm#L251](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L251)
- [_WKWebsiteDataStoreConfiguration.mm#L256](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L256)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
