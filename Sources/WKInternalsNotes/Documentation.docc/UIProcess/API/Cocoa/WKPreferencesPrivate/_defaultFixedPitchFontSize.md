# ``WKInternalsNotes/WKPreferences/_defaultFixedPitchFontSize``

Default Fixed Font Size を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDefaultFixedPitchFontSize:) NSUInteger _defaultFixedPitchFontSize WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `13` / macOS: `13`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_defaultFixedPitchFontSize` を設定すると: Default Fixed Font Size を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/style/StyleBuilderState.cpp#L216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleBuilderState.cpp#L216) の `Style::fontSizeForKeyword` が `defaultFixedFontSize()` を参照する。

## Details
- WebPreferences key: `DefaultFixedFontSize`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L104`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L104)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L536`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L536)
- [`Source/WebCore/style/StyleBuilderState.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleBuilderState.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2296`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2296) (key: `DefaultFixedFontSize`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
