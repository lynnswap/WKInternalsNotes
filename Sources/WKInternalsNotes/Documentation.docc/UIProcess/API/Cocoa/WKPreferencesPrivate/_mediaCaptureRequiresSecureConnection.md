# ``WKInternalsNotes/WKPreferences/_mediaCaptureRequiresSecureConnection``

Limit Media Capture to Secure Sites を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaCaptureRequiresSecureConnection:) BOOL _mediaCaptureRequiresSecureConnection WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_mediaCaptureRequiresSecureConnection = YES`: Limit Media Capture to Secure Sites を有効化する。
- `_mediaCaptureRequiresSecureConnection = NO`: Limit Media Capture to Secure Sites を無効化する。
- Implementation: [`Source/WebCore/dom/ScriptExecutionContext.cpp#L696`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/ScriptExecutionContext.cpp#L696) の `ScriptExecutionContext::allowsMediaDevices` が `mediaCaptureRequiresSecureConnection()` を参照する。

## Details
- WebPreferences key: `MediaCaptureRequiresSecureConnection`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L121)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L710`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L710)
- [`Source/WebCore/dom/ScriptExecutionContext.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/ScriptExecutionContext.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4884`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4884) (key: `MediaCaptureRequiresSecureConnection`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
