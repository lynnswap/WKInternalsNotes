# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/alternativeServicesStorageDirectory``

Alternative Services の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *alternativeServicesStorageDirectory WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `alternativeServicesDirectory` の値を返す。

## Discussion
getter は `_configuration->alternativeServicesDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setAlternativeServicesDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L98](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L98)
- [_WKWebsiteDataStoreConfiguration.mm#L384](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L384)
- [_WKWebsiteDataStoreConfiguration.mm#L389](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L389)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
