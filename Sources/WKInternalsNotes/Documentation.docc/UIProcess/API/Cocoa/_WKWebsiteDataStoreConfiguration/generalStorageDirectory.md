# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/generalStorageDirectory``

General Storage の保存先ディレクトリを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSURL *generalStorageDirectory WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
`generalStorageDirectory` が未設定なら `nil` を返す。

## Discussion
getter は `_configuration->generalStorageDirectory()` が `isNull()` の場合は `nil` を返し、それ以外はディレクトリ URL を作成する。setter は永続ストア以外または identifier 付き構成では例外を投げ、file URL を検証した上で `setGeneralStorageDirectory` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L100](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L100)
- [_WKWebsiteDataStoreConfiguration.mm#L401](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L401)
- [_WKWebsiteDataStoreConfiguration.mm#L409](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L409)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
