# ``WKInternalsNotes/WKPreferences/_isEnabledForExperimentalFeature(_:)``

`_WKExperimentalFeature` の有効状態を返す

## Objective-C Declaration
```objective-c
- (BOOL)_isEnabledForExperimentalFeature:(_WKExperimentalFeature *)feature WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: `_WKExperimentalFeature` の有効状態を返す。

## References
- [`WKPreferencesPrivate.h#L148`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L148)
- [`WKPreferences.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L594)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
