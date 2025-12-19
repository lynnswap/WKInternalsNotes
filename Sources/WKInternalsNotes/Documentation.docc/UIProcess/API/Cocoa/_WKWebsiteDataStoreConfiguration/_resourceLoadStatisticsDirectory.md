# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_resourceLoadStatisticsDirectory``

Resource Load Statistics の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setResourceLoadStatisticsDirectory:) NSURL *_resourceLoadStatisticsDirectory WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `resourceLoadStatisticsDirectory` の値を返す。

## Discussion
getter は `_configuration->resourceLoadStatisticsDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setResourceLoadStatisticsDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L79](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L79)
- [_WKWebsiteDataStoreConfiguration.mm#L234](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L234)
- [_WKWebsiteDataStoreConfiguration.mm#L239](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L239)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
