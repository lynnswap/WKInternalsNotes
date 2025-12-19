# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_indexedDBDatabaseDirectory``

IndexedDB の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setIndexedDBDatabaseDirectory:) NSURL *_indexedDBDatabaseDirectory;
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `indexedDBDatabaseDirectory` の値を返す。

## Discussion
getter は `_configuration->indexedDBDatabaseDirectory()` からディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setIndexedDBDatabaseDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L76](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L76)
- [_WKWebsiteDataStoreConfiguration.mm#L126](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L126)
- [_WKWebsiteDataStoreConfiguration.mm#L131](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L131)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
