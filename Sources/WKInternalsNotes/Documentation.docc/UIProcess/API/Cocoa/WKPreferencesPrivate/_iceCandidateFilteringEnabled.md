# ``WKInternalsNotes/WKPreferences/_iceCandidateFilteringEnabled``

ICE Candidate Filtering を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setICECandidateFilteringEnabled:) BOOL _iceCandidateFilteringEnabled WK_API_AVAILABLE(macos(10.13.4), ios(11.3));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_iceCandidateFilteringEnabled = YES`: ICE Candidate Filtering を有効化する。
- `_iceCandidateFilteringEnabled = NO`: ICE Candidate Filtering を無効化する。
- Implementation: [`Source/WebCore/page/SettingsBase.cpp#L397`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp#L397) の `SettingsBase::iceCandidateFilteringEnabledChanged` が `iceCandidateFilteringEnabled()` を参照する。

## Details
- WebPreferences key: `ICECandidateFilteringEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L123`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L123)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L760)
- [`Source/WebCore/page/SettingsBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/SettingsBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3481`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3481) (key: `ICECandidateFilteringEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
