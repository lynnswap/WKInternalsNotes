# ``WKInternalsNotes/WKPreferencesPrivate/_pitchCorrectionAlgorithm``

Pitch Correction Algorithm を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPitchCorrectionAlgorithm:) _WKPitchCorrectionAlgorithm _pitchCorrectionAlgorithm WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Default Value
iOS: `static_cast<uint32_t>(WebCore::MediaPlayerEnums::PitchCorrectionAlgorithm::BestAllAround)` / macOS: `static_cast<uint32_t>(WebCore::MediaPlayerEnums::PitchCorrectionAlgorithm::BestAllAround)`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_pitchCorrectionAlgorithm` を設定すると: Pitch Correction Algorithm を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/html/HTMLMediaElement.cpp#L1895`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp#L1895) の `DiagnosticLoggingKeys::videoKey` が `pitchCorrectionAlgorithm()` を参照する。

## Details
- WebPreferences key: `PitchCorrectionAlgorithm`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L175`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L175)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1459`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1459)
- [`Source/WebCore/html/HTMLMediaElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLMediaElement.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6039`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6039) (key: `PitchCorrectionAlgorithm`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
