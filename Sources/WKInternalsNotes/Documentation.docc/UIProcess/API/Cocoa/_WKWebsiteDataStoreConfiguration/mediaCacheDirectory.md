# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/mediaCacheDirectory``

メディアキャッシュの保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *mediaCacheDirectory WK_API_AVAILABLE(macos(10.15.4), ios(13.4));
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `mediaCacheDirectory` の値を返す。

## Discussion
getter は `_configuration->mediaCacheDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setMediaCacheDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L87](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L87)
- [_WKWebsiteDataStoreConfiguration.mm#L333](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L333)
- [_WKWebsiteDataStoreConfiguration.mm#L338](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L338)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
