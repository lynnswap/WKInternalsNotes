# ``WKInternalsNotes/WKPreferences/_backspaceKeyNavigationEnabled``

Backspace Key Navigation を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setBackspaceKeyNavigationEnabled:) BOOL _backspaceKeyNavigationEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_backspaceKeyNavigationEnabled = YES`: Backspace Key Navigation を有効化する。
- `_backspaceKeyNavigationEnabled = NO`: Backspace Key Navigation を無効化する。
- Implementation: [`EventHandler.cpp#L4992`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/EventHandler.cpp#L4992) の `EventHandler::defaultBackspaceEventHandler` が `backspaceKeyNavigationEnabled()` を参照する。

## Details
- WebPreferences key: `BackspaceKeyNavigationEnabled`

## References
- [`WKPreferencesPrivate.h#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L223)
- [`WKPreferences.mm#L1159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1159)
- [`EventHandler.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/EventHandler.cpp)
- [`UnifiedWebPreferences.yaml#L764`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L764) (key: `BackspaceKeyNavigationEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
