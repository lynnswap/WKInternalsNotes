# ``WKInternalsNotes/WKWebpagePreferences/_captivePortalModeEnabled``

Lockdown mode（captive portal）を有効/無効にする。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCaptivePortalModeEnabled:) BOOL _captivePortalModeEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
初期値は `WebsitePolicies::lockdownModeEnabled()` に依存し、明示設定がなければシステムのロックダウン状態を使う。

## Discussion
setter は `setLockdownModeEnabled` を呼ぶ。iOS では無効化時に entitlements がない場合 `NSInternalInconsistencyException` を投げる。getter は `lockdownModeEnabled()` を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L117)
- [`WKWebpagePreferences.mm#L523`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L523)
- [`WKWebpagePreferences.mm#L523`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L523)
- [`APIWebsitePolicies.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIWebsitePolicies.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
