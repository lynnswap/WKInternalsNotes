# ``WKInternalsNotes/WKPreferences/_mediaStreamEnabled``

no-op（常に `YES`）

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaStreamEnabled:) BOOL _mediaStreamEnabled WK_API_DEPRECATED("Media stream preference is no longer supported", macos(10.14, 15.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 常に `YES`。
- この API で値を設定しても: 実装が no-op のため挙動は変わらない。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L262)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1918`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1918)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
