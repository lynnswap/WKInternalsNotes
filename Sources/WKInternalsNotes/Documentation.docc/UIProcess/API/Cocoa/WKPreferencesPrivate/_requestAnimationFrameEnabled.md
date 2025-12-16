# ``WKInternalsNotes/WKPreferencesPrivate/_requestAnimationFrameEnabled``

no-op（常に `YES`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setRequestAnimationFrameEnabled:) BOOL _requestAnimationFrameEnabled WK_API_DEPRECATED("requestAnimationFrame is always enabled", macos(10.15.4, 13.0), ios(13.4, 16.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 常に `YES`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L248)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1813`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1813)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
