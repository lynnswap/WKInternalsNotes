# ``WKInternalsNotes/WKPreferences/_speechRecognitionEnabled``

SpeechRecognition API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSpeechRecognitionEnabled:) BOOL _speechRecognitionEnabled WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_speechRecognitionEnabled = YES`: SpeechRecognition API を有効化する。
- `_speechRecognitionEnabled = NO`: SpeechRecognition API を無効化する。
- Implementation: [`Source/WebCore/Modules/speech/SpeechRecognition.idl#L28`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/speech/SpeechRecognition.idl#L28)（`EnabledBySetting=SpeechRecognitionEnabled`）

## Details
- WebPreferences key: `SpeechRecognitionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L172`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L172)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1429`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1429)
- [`Source/WebCore/Modules/speech/SpeechRecognition.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/speech/SpeechRecognition.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7565`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7565) (key: `SpeechRecognitionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
