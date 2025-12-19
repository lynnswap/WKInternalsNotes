# ``WKInternalsNotes/WKWebpagePreferences/_visibilityAdjustmentSelectorsIncludingShadowHosts``

視認性調整対象のセレクタ（shadow host 含む）を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setVisibilityAdjustmentSelectorsIncludingShadowHosts:) NSArray<NSArray<NSSet<NSString *> *> *> *_visibilityAdjustmentSelectorsIncludingShadowHosts WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
初期値は `visibilityAdjustmentSelectors()` の内容に依存する。

## Discussion
setter は多重配列/集合を `TargetedElementSelectors` の vector に変換して設定する。getter は保持している selectors を NSArray/NSSet に戻して返す。

## References
- [`WKWebpagePreferencesPrivate.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L125)
- [`WKWebpagePreferences.mm#L732`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L732)
- [`WKWebpagePreferences.mm#L751`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L751)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
