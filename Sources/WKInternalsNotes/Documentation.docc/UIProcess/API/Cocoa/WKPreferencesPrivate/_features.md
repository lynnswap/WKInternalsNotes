# ``WKInternalsNotes/WKPreferencesPrivate/_features()``

利用可能な `_WKFeature` 一覧を返す

## Objective-C Declaration
```objective-c
+ (NSArray<_WKFeature *> *)_features WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: 利用可能な `_WKFeature` 一覧を返す。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L139)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L556`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L556)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
