# ``WKInternalsNotes/WKPreferences/_dnsPrefetchingEnabled``

no-op（常に `NO`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDNSPrefetchingEnabled:) BOOL _dnsPrefetchingEnabled WK_API_DEPRECATED("DNS prefetching is no longer supported", macos(10.14, 26.0));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 常に `NO`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`WKPreferencesPrivate.h#L251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L251)
- [`WKPreferences.mm#L1795`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1795)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
