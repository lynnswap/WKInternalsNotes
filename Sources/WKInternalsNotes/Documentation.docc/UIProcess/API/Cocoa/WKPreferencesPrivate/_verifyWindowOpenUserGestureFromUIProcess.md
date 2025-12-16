# ``WKInternalsNotes/WKPreferencesPrivate/_verifyWindowOpenUserGestureFromUIProcess``

Verify window.open user gesture を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setVerifyWindowOpenUserGestureFromUIProcess:) BOOL _verifyWindowOpenUserGestureFromUIProcess WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_verifyWindowOpenUserGestureFromUIProcess = YES`: Verify window.open user gesture を有効化する。
- `_verifyWindowOpenUserGestureFromUIProcess = NO`: Verify window.open user gesture を無効化する。
- Implementation: [`Source/WebKit/UIProcess/WebPageProxy.cpp#L955`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp#L955) の `LinkDecorationFilteringController::sharedSingleton` が `verifyWindowOpenUserGestureFromUIProcess()` を参照する。

## Details
- WebPreferences key: `VerifyWindowOpenUserGestureFromUIProcess`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L191)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1630`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1630)
- [`Source/WebKit/UIProcess/WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8547`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8547) (key: `VerifyWindowOpenUserGestureFromUIProcess`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
