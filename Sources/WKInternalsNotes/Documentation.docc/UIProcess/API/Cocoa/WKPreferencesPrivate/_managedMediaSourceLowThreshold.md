# ``WKInternalsNotes/WKPreferences/_managedMediaSourceLowThreshold``

Managed Media Source Low Threshold を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setManagedMediaSourceLowThreshold:) double _managedMediaSourceLowThreshold WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `10` / macOS: `10`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_managedMediaSourceLowThreshold` を設定すると: Managed Media Source Low Threshold を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`ManagedMediaSource.cpp#L101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/ManagedMediaSource.cpp#L101) の `ManagedMediaSource::ensurePrefsRead` が `settingsValues().managedMediaSourceLowThreshold` を読み出す。

## Details
- WebPreferences key: `ManagedMediaSourceLowThreshold`

## References
- [`WKPreferencesPrivate.h#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L193)
- [`WKPreferences.mm#L938`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L938)
- [`ManagedMediaSource.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/ManagedMediaSource.cpp)
- [`UnifiedWebPreferences.yaml#L4760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4760) (key: `ManagedMediaSourceLowThreshold`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
