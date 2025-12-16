# ``WKInternalsNotes/WKPreferencesPrivate/_experimentalFeatures()``

利用可能な `_WKExperimentalFeature` 一覧を返す

## Objective-C Declaration
```objective-c
+ (NSArray<_WKExperimentalFeature *> *)_experimentalFeatures WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: 利用可能な `_WKExperimentalFeature` 一覧を返す。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L147`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L147)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L578`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L578)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
