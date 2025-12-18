# ``WKInternalsNotes/WKPreferences/_webAudioEnabled``

Web Audio を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWebAudioEnabled:) BOOL _webAudioEnabled WK_API_AVAILABLE(macos(10.14), ios(13.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_webAudioEnabled = YES`: Web Audio を有効化する。
- `_webAudioEnabled = NO`: Web Audio を無効化する。
- Implementation: [`AnalyserNode.idl#L27`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AnalyserNode.idl#L27)（`EnabledBySetting=WebAudioEnabled`）

## Details
- WebPreferences key: `WebAudioEnabled`

## References
- [`WKPreferencesPrivate.h#L168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L168)
- [`WKPreferences.mm#L968`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L968)
- [`AnalyserNode.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AnalyserNode.idl)
- [`UnifiedWebPreferences.yaml#L8932`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8932) (key: `WebAudioEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
