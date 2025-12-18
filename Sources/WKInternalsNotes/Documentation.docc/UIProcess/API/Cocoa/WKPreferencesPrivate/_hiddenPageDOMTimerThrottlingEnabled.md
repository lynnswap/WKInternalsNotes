# ``WKInternalsNotes/WKPreferences/_hiddenPageDOMTimerThrottlingEnabled``

hidden page DOM timer throttling を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setHiddenPageDOMTimerThrottlingEnabled:) BOOL _hiddenPageDOMTimerThrottlingEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_hiddenPageDOMTimerThrottlingEnabled = YES`: hidden page DOM timer throttling を有効化する。
- `_hiddenPageDOMTimerThrottlingEnabled = NO`: hidden page DOM timer throttling を無効化する。
- Implementation: [`Source/WebCore/page/Page.cpp#L2949`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp#L2949) の `Page::updateTimerThrottlingState` が `hiddenPageDOMTimerThrottlingEnabled()` を参照する。

## Details
- WebPreferences key: `HiddenPageDOMTimerThrottlingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L92)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L456`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L456)
- [`Source/WebCore/page/Page.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3438`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3438) (key: `HiddenPageDOMTimerThrottlingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
