# ``WKInternalsNotes/WKPreferencesPrivate/_defaultFontSize``

Default Font Size を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDefaultFontSize:) NSUInteger _defaultFontSize WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `16` / macOS: `16`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_defaultFontSize` を設定すると: Default Font Size を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/style/StyleBuilderState.cpp#L216`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleBuilderState.cpp#L216) の `Style::fontSizeForKeyword` が `defaultFontSize()` を参照する。

## Details
- WebPreferences key: `DefaultFontSize`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L103`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L103)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L526`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L526)
- [`Source/WebCore/style/StyleBuilderState.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/StyleBuilderState.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2308`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2308) (key: `DefaultFontSize`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
