# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/volumeCapacityOverride``

ボリューム容量の上書き値を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSNumber *volumeCapacityOverride WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
未設定の場合は `nil` を返す。

## Discussion
getter は `_configuration->volumeCapacityOverride()` が `std::nullopt` の場合に `nil` を返し、設定されていれば `NSNumber` に変換して返す。setter は `NSNumber` を `std::optional<uint64_t>` に変換して設定する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L103](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L103)
- [_WKWebsiteDataStoreConfiguration.mm#L565](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L565)
- [_WKWebsiteDataStoreConfiguration.mm#L574](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L574)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
