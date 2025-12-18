# ``WKInternalsNotes/WKPreferences/_isEnabledForInternalDebugFeature(_:)``

`_WKInternalDebugFeature` の有効状態を返す

## Objective-C Declaration
```objective-c
- (BOOL)_isEnabledForInternalDebugFeature:(_WKInternalDebugFeature *)feature WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: `_WKInternalDebugFeature` の有効状態を返す。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L144)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L568`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L568)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
