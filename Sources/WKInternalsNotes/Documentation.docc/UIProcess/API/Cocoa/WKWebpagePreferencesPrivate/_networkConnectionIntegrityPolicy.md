# ``WKInternalsNotes/WKWebpagePreferences/_networkConnectionIntegrityPolicy``

ネットワーク整合性保護の詳細ポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNetworkConnectionIntegrityPolicy:) _WKWebsiteNetworkConnectionIntegrityPolicy _networkConnectionIntegrityPolicy WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
初期値は advancedPrivacyProtections の状態に依存する。

## Discussion
getter は `advancedPrivacyProtections` を `_WKWebsiteNetworkConnectionIntegrityPolicy` のビット列へ変換する。setter はビット列を `AdvancedPrivacyProtections` の OptionSet に変換して設定する。

## References
- [`WKWebpagePreferencesPrivate.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L123)
- [`WKWebpagePreferences.mm#L651`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L651)
- [`WKWebpagePreferences.mm#L692`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L692)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
