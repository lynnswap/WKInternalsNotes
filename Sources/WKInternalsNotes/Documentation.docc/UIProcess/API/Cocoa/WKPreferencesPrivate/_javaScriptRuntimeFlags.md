# ``WKInternalsNotes/WKPreferencesPrivate/_javaScriptRuntimeFlags``

JavaScript Runtime Flags を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setJavaScriptRuntimeFlags:) _WKJavaScriptRuntimeFlags _javaScriptRuntimeFlags WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `0` / macOS: `0`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_javaScriptRuntimeFlags` を設定すると: JavaScript Runtime Flags を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/Modules/webaudio/AudioWorkletMessagingProxy.cpp#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AudioWorkletMessagingProxy.cpp#L50) で `javaScriptRuntimeFlags()` が参照される。

## Details
- WebPreferences key: `JavaScriptRuntimeFlags`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L97)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L496`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L496)
- [`Source/WebCore/Modules/webaudio/AudioWorkletMessagingProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/webaudio/AudioWorkletMessagingProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4235`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4235) (key: `JavaScriptRuntimeFlags`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
