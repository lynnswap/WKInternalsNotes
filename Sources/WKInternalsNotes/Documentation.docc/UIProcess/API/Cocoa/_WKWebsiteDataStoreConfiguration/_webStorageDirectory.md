# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/_webStorageDirectory``

Web Storage の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setWebStorageDirectory:) NSURL *_webStorageDirectory;
```

## Default Value
`WebsiteDataStoreConfiguration` が保持する `localStorageDirectory` の値を返す。

## Discussion
getter は `_configuration->localStorageDirectory()` のパスからディレクトリ URL を作成して返す。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setLocalStorageDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L75](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L75)
- [_WKWebsiteDataStoreConfiguration.mm#L109](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L109)
- [_WKWebsiteDataStoreConfiguration.mm#L114](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L114)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
