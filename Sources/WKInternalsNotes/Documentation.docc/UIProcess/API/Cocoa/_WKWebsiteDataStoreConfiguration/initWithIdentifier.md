# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/initWithIdentifier(_:)``

識別子付きの永続構成を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithIdentifier:(NSUUID *)identifier WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
identifier が `nil` または無効な場合は例外を投げる。`WTF::UUID::fromNSUUID` で変換した UUID を用いて `constructInWrapper` を呼ぶ。

## References
- [_WKWebsiteDataStoreConfiguration.h#L42](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L42)
- [_WKWebsiteDataStoreConfiguration.mm#L63](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L63)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
