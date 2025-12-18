# ``WKInternalsNotes/WKPreferences/_disableMediaPlaybackRelatedFeatures()``

media playback 関連 features をまとめて無効化する

## Objective-C Declaration
```objective-c
- (void)_disableMediaPlaybackRelatedFeatures;
```

## Discussion
- このメソッドを使わない場合: 既定の設定のまま動作する。
- 呼び出すと: media playback 関連 features をまとめて無効化する。

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L151)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L609`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L609)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
