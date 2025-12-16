# ``WKInternalsNotes/WKPreferencesPrivate/_mediaPreferredFullscreenWidth``

Media Preferred Fullscreen Width を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaPreferredFullscreenWidth:) double _mediaPreferredFullscreenWidth WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
iOS: `960` / macOS: `960`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaPreferredFullscreenWidth` を設定すると: Media Preferred Fullscreen Width を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm#L902`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm#L902) の `PAL::currentUserInterfaceIdiomIsVision` が `mediaPreferredFullscreenWidth()` を参照する。

## Details
- WebPreferences key: `MediaPreferredFullscreenWidth`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L189`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L189)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1610`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1610)
- [`Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WebPageProxyIOS.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5034`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5034) (key: `MediaPreferredFullscreenWidth`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
