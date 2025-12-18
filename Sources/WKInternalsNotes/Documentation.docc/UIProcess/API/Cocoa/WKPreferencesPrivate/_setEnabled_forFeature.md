# ``WKInternalsNotes/WKPreferences/_setEnabled(_:forFeature:)``

`_WKFeature` の有効状態を更新する

## Objective-C Declaration
```objective-c
- (void)_setEnabled:(BOOL)value forFeature:(_WKFeature *)feature WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: `_WKFeature` の有効状態を更新する。

## References
- [`WKPreferencesPrivate.h#L141`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L141)
- [`WKPreferences.mm#L573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
