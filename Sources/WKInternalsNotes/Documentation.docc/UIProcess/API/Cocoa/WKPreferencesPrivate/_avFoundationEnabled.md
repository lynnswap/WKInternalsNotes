# ``WKInternalsNotes/WKPreferencesPrivate/_avFoundationEnabled``

AVFoundation を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAVFoundationEnabled:) BOOL _avFoundationEnabled WK_API_AVAILABLE(macos(10.10), ios(12.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_avFoundationEnabled = YES`: AVFoundation を有効化する。
- `_avFoundationEnabled = NO`: AVFoundation を無効化する。
- Implementation: [`Source/WebCore/page/DeprecatedGlobalSettings.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L39) で `isAVFoundationEnabled()` が参照される。

## Details
- WebPreferences key: `AVFoundationEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L135)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L838`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L838)
- [`Source/WebCore/page/DeprecatedGlobalSettings.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L69) (key: `AVFoundationEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
