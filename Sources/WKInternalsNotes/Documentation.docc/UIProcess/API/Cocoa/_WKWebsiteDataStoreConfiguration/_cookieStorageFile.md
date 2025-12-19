# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_cookieStorageFile``

Cookie 保存ファイルのパスを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setCookieStorageFile:) NSURL *_cookieStorageFile;
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `cookieStorageFile` の値を返す。

## Discussion
getter は `_configuration->cookieStorageFile()` からファイル URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL かつディレクトリではないことを検証した上で `setCookieStorageFile` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L78](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L78)
- [_WKWebsiteDataStoreConfiguration.mm#L214](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L214)
- [_WKWebsiteDataStoreConfiguration.mm#L219](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L219)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
