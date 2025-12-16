# ``WKInternalsNotes/WKPreferencesPrivate/_viewGestureDebuggingEnabled``

view gesture debugging を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setViewGestureDebuggingEnabled:) BOOL _viewGestureDebuggingEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_viewGestureDebuggingEnabled = YES`: view gesture debugging を有効化する。
- `_viewGestureDebuggingEnabled = NO`: view gesture debugging を無効化する。
- Implementation: [`Source/WebKit/UIProcess/mac/ViewGestureControllerMac.mm#L397`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/ViewGestureControllerMac.mm#L397) の `ViewGestureController::beginSwipeGesture` が `viewGestureDebuggingEnabled()` を参照する。

## Details
- WebPreferences key: `ViewGestureDebuggingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L221)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1139)
- [`Source/WebKit/UIProcess/mac/ViewGestureControllerMac.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/ViewGestureControllerMac.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8682`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8682) (key: `ViewGestureDebuggingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
