# ``WKInternalsNotes/WKPreferencesPrivate/_internalDebugFeatures()``

利用可能な `_WKInternalDebugFeature` 一覧を返す

## Objective-C Declaration
```objective-c
+ (NSArray<_WKInternalDebugFeature *> *)_internalDebugFeatures WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: 利用可能な `_WKInternalDebugFeature` 一覧を返す。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L143`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L143)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L562`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L562)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
