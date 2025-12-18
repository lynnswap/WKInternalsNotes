# ``WKInternalsNotes/WKPreferences/_disableRichJavaScriptFeatures()``

rich JavaScript features をまとめて無効化する

## Objective-C Declaration
```objective-c
- (void)_disableRichJavaScriptFeatures;
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: rich JavaScript features をまとめて無効化する。

## References
- [`WKPreferencesPrivate.h#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L150)
- [`WKPreferences.mm#L604`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L604)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
