# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/persistent``

永続構成かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=isPersistent) BOOL persistent WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Default Value
`_configuration->isPersistent()` の結果を返す。

## Discussion
getter は `_configuration->isPersistent()` の値を返す。

## References
- [_WKWebsiteDataStoreConfiguration.h#L40](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L40)
- [_WKWebsiteDataStoreConfiguration.mm#L104](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L104)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
