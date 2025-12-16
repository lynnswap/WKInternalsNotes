# ``WKInternalsNotes/WKPreferencesPrivate/_hiddenPageDOMTimerThrottlingAutoIncreases``

Hidden page DOM timer throttling auto-increases を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setHiddenPageDOMTimerThrottlingAutoIncreases:) BOOL _hiddenPageDOMTimerThrottlingAutoIncreases WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_hiddenPageDOMTimerThrottlingAutoIncreases = YES`: Hidden page DOM timer throttling auto-increases を有効化する。
- `_hiddenPageDOMTimerThrottlingAutoIncreases = NO`: Hidden page DOM timer throttling auto-increases を無効化する。
- Implementation: [`Source/WebCore/page/Page.cpp#L2949`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp#L2949) の `Page::updateTimerThrottlingState` が `hiddenPageDOMTimerThrottlingAutoIncreases()` を参照する。

## Details
- WebPreferences key: `HiddenPageDOMTimerThrottlingAutoIncreases`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L93)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L466)
- [`Source/WebCore/page/Page.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/Page.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3425`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3425) (key: `HiddenPageDOMTimerThrottlingAutoIncreases`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
