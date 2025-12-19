# ``WKInternalsNotes/WKWebpagePreferences/_networkConnectionIntegrityEnabled``

ネットワーク整合性保護の一括有効状態を示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setNetworkConnectionIntegrityEnabled:) BOOL _networkConnectionIntegrityEnabled WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
初期値は advancedPrivacyProtections の状態に依存し、4種すべて含まれる場合のみ `YES`。

## Discussion
getter は Baseline/Fingerprinting/EnhancedNetworkPrivacy/LinkDecorationFiltering が全て有効かを確認する。setter は同じ 4 つのフラグを一括で切り替える。

## References
- [`WKWebpagePreferencesPrivate.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L122)
- [`WKWebpagePreferences.mm#L631`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L631)
- [`WKWebpagePreferences.mm#L631`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L631)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
