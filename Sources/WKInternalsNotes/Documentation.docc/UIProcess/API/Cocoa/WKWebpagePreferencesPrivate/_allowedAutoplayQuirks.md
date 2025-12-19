# ``WKInternalsNotes/WKWebpagePreferences/_allowedAutoplayQuirks``

autoplay の quirk 許可フラグを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAllowedAutoplayQuirks:) _WKWebsiteAutoplayQuirk _allowedAutoplayQuirks;
```

## Default Value
初期値は `WebsitePolicies::allowedAutoplayQuirks()` の状態に依存する。

## Discussion
setter は `_WKWebsiteAutoplayQuirk` のビットを `WebsiteAutoplayQuirk` の OptionSet に変換して設定する。getter は `allowedAutoplayQuirks()` の内容から対応するビットを組み立てる。

## References
- [`WKWebpagePreferencesPrivate.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L100)
- [`WKWebpagePreferences.mm#L269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L269)
- [`WKWebpagePreferences.mm#L269`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L269)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
