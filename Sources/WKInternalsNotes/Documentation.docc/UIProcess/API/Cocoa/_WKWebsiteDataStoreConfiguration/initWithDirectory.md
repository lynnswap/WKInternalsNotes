# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/initWithDirectory(_:)``

指定ディレクトリを使用する構成を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithDirectory:(NSURL *)directory WK_API_AVAILABLE(macos(15.2), ios(18.2), visionos(2.2));
```

## Discussion
directory が `nil` の場合は例外を投げる。`directory.path` を取得し、同じパスを渡して `constructInWrapper` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L43](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L43)
- [_WKWebsiteDataStoreConfiguration.mm#L81](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L81)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
