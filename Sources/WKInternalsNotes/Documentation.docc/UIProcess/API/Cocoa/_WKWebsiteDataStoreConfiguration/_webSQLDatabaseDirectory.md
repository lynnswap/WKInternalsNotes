# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_webSQLDatabaseDirectory``

WebSQL の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setWebSQLDatabaseDirectory:) NSURL *_webSQLDatabaseDirectory;
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `webSQLDatabaseDirectory` の値を返す。

## Discussion
getter は `_configuration->webSQLDatabaseDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setWebSQLDatabaseDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L77](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L77)
- [_WKWebsiteDataStoreConfiguration.mm#L177](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L177)
- [_WKWebsiteDataStoreConfiguration.mm#L182](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L182)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
