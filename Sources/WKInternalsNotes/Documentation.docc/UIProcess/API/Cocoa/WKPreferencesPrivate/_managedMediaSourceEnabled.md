# ``WKInternalsNotes/WKPreferences/_managedMediaSourceEnabled``

Managed Media Source API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setManagedMediaSourceEnabled:) BOOL _managedMediaSourceEnabled  WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `WebKit::defaultManagedMediaSourceEnabled()` / macOS: `WebKit::defaultManagedMediaSourceEnabled()`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_managedMediaSourceEnabled = YES`: Managed Media Source API を有効化する。
- `_managedMediaSourceEnabled = NO`: Managed Media Source API を無効化する。
- Implementation: [`Source/WebCore/Modules/mediasource/BufferedChangeEvent.idl#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/BufferedChangeEvent.idl#L28)（`EnabledBySetting=ManagedMediaSourceEnabled`）

## Details
- WebPreferences key: `ManagedMediaSourceEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L192)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L928`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L928)
- [`Source/WebCore/Modules/mediasource/BufferedChangeEvent.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/mediasource/BufferedChangeEvent.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4732`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4732) (key: `ManagedMediaSourceEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
