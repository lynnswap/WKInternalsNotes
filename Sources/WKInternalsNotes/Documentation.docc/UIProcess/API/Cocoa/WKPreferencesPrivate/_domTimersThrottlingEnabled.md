# ``WKInternalsNotes/WKPreferences/_domTimersThrottlingEnabled``

DOM timer throttling を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDOMTimersThrottlingEnabled:) BOOL _domTimersThrottlingEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_domTimersThrottlingEnabled = YES`: DOM timer throttling を有効化する。
- `_domTimersThrottlingEnabled = NO`: DOM timer throttling を無効化する。
- Implementation: [`DOMTimer.cpp#L257`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DOMTimer.cpp#L257) の `DOMTimer::isDOMTimersThrottlingEnabled` が `domTimersThrottlingEnabled()` を参照する。

## Details
- WebPreferences key: `DOMTimersThrottlingEnabled`

## References
- [`WKPreferencesPrivate.h#L211`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L211)
- [`WKPreferences.mm#L1039`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1039)
- [`DOMTimer.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DOMTimer.cpp)
- [`UnifiedWebPreferences.yaml#L2197`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2197) (key: `DOMTimersThrottlingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
