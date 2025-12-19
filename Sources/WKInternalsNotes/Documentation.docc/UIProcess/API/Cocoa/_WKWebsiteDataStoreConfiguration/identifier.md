# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/identifier``

構成の識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSUUID *identifier WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
未設定の場合は `nil` を返す。

## Discussion
`_configuration->identifier()` が空の場合は `nil` を返し、設定されていれば `NSUUID` に変換して返す。

## References
- [_WKWebsiteDataStoreConfiguration.h#L42](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L42)
- [_WKWebsiteDataStoreConfiguration.mm#L854](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L854)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
