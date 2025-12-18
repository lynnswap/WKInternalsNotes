# ``WKInternalsNotes/WKPreferences/_useSystemAppearance``

System Appearance を使用する設定。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUseSystemAppearance:) BOOL _useSystemAppearance;
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- `WKPreferences` の内部 `WebPreferences` にある `useSystemAppearance` を切り替える。

## Details
- WebPreferences key: `UseSystemAppearance`

## References
- [`WKPreferencesInternal.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesInternal.h#L59)
- [`WKPreferences.mm#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L225)
- [`UnifiedWebPreferences.yaml#L8431`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8431) (key: `UseSystemAppearance`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-18 |
