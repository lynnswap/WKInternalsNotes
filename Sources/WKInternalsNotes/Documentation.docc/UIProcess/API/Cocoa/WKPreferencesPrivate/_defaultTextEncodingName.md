# ``WKInternalsNotes/WKPreferences/_defaultTextEncodingName``

Default Text Encoding Name を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDefaultTextEncodingName:) NSString *_defaultTextEncodingName WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `PAL::defaultTextEncodingNameForSystemLanguage()`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_defaultTextEncodingName` を設定すると: Default Text Encoding Name を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/dom/Document.cpp#L2198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L2198) の `Document::defaultCharsetForLegacyBindings` が `defaultTextEncodingName()` を参照する。

## Details
- WebPreferences key: `DefaultTextEncodingName`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L209`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L209)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1019`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1019)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2320) (key: `DefaultTextEncodingName`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
