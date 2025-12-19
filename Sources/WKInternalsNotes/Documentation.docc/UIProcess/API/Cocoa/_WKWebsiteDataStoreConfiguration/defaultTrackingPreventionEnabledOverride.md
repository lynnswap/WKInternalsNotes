# ``WKInternalsNotes/_WKWebsiteDataStoreConfiguration/defaultTrackingPreventionEnabledOverride``

トラッキング防止の既定値上書きを返す/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy) NSNumber *defaultTrackingPreventionEnabledOverride WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
未設定の場合は `nil` を返す。

## Discussion
getter は `_configuration->defaultTrackingPreventionEnabledOverride()` が `std::nullopt` の場合に `nil` を返し、設定されていれば `NSNumber` に変換して返す。setter は `NSNumber` を `std::optional<bool>` に変換して設定する。

## References
- [_WKWebsiteDataStoreConfiguration.h#L105](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.h#L105)
- [_WKWebsiteDataStoreConfiguration.mm#L836](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L836)
- [_WKWebsiteDataStoreConfiguration.mm#L845](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKWebsiteDataStoreConfiguration.mm#L845)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
