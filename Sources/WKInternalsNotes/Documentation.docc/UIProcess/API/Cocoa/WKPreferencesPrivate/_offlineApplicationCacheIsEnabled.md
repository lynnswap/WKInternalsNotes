# ``WKInternalsNotes/WKPreferencesPrivate/_offlineApplicationCacheIsEnabled``

no-op（常に `NO`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOfflineApplicationCacheIsEnabled:) BOOL _offlineApplicationCacheIsEnabled WK_API_DEPRECATED("OfflineApplicationCache is no longer supported", macos(10.10, WK_MAC_TBA), ios(8.0, WK_IOS_TBA));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 常に `NO`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L261`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L261)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1905`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1905)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
