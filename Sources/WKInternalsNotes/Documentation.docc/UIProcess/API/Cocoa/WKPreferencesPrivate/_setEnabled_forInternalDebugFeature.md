# ``WKInternalsNotes/WKPreferences/_setEnabled(_:forInternalDebugFeature:)``

`_WKInternalDebugFeature` の有効状態を更新する

## Objective-C Declaration
```objective-c
- (void)_setEnabled:(BOOL)value forInternalDebugFeature:(_WKInternalDebugFeature *)feature WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: `_WKInternalDebugFeature` の有効状態を更新する。

## References
- [`WKPreferencesPrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L141)
- [`WKPreferences.mm#L573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
