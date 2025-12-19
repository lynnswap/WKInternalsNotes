# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/originQuotaRatio``

Origin quota の比率を返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSNumber *originQuotaRatio WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
未設定の場合は `nil` を返す。

## Discussion
getter は `_configuration->originQuotaRatio()` が `std::nullopt` の場合に `nil` を返す。setter は 0.0〜1.0 の範囲外なら例外を投げ、範囲内なら `setOriginQuotaRatio` に委譲する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L56](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L56)
- [_WKWebsiteDataStoreConfiguration.mm#L505](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L505)
- [_WKWebsiteDataStoreConfiguration.mm#L514](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L514)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
