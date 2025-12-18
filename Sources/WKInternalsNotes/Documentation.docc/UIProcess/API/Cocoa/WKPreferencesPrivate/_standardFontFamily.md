# ``WKInternalsNotes/WKPreferences/_standardFontFamily``

Standard Font Family を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStandardFontFamily:) NSString *_standardFontFamily WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `"Times"_str`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_standardFontFamily` を設定すると: Standard Font Family を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`CSSFontFaceSet.cpp#L324`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/CSSFontFaceSet.cpp#L324) の `WTF::switchOn` が `standardFontFamily()` を参照する。

## Details
- WebPreferences key: `StandardFontFamily`

## References
- [`WKPreferencesPrivate.h#L222`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L222)
- [`WKPreferences.mm#L1149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1149)
- [`CSSFontFaceSet.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/css/CSSFontFaceSet.cpp)
- [`UnifiedWebPreferences.yaml#L7625`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7625) (key: `StandardFontFamily`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
