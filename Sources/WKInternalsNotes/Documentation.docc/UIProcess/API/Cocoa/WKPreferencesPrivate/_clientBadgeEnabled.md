# ``WKInternalsNotes/WKPreferencesPrivate/_clientBadgeEnabled``

no-op（常に `NO`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setClientBadgeEnabled:) BOOL _clientBadgeEnabled WK_API_DEPRECATED("Client badge is no longer supported", macos(13.3, 26.0), ios(16.4, 26.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 常に `NO`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L263`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L263)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1927`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1927)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
