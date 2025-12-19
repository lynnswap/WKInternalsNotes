# ``WKInternalsNotes/WKWebpagePreferences/_visibilityAdjustmentSelectors``

視認性調整対象のセレクタ（shadow host を除外）を設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, setter=_setVisibilityAdjustmentSelectors:) NSSet<NSString *> *_visibilityAdjustmentSelectors WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Default Value
初期値は `visibilityAdjustmentSelectors()` の内容に依存する。

## Discussion
setter は各 selector を 1 要素のセットとしてラップし、`_visibilityAdjustmentSelectorsIncludingShadowHosts` に委譲する。getter は shadow root を含む selector 群を除外して返す。

## References
- [`WKWebpagePreferencesPrivate.h#L126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L126)
- [`WKWebpagePreferences.mm#L767`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L767)
- [`WKWebpagePreferences.mm#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L775)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
