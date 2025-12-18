# ``WKInternalsNotes/WKPreferences/_pdfPluginEnabled``

PDF Plugin を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setPDFPluginEnabled:) BOOL _pdfPluginEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_pdfPluginEnabled = YES`: PDF Plugin を有効化する。
- `_pdfPluginEnabled = NO`: PDF Plugin を無効化する。
- Implementation: [`Source/WebKit/WebProcess/Plugins/WebPluginInfoProvider.cpp#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/Plugins/WebPluginInfoProvider.cpp#L45) の `WebPluginInfoProvider::refreshPlugins` が `pdfPluginEnabled()` を参照する。

## Details
- WebPreferences key: `PDFPluginEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L231`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L231)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1249`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1249)
- [`Source/WebKit/WebProcess/Plugins/WebPluginInfoProvider.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/Plugins/WebPluginInfoProvider.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5793`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5793) (key: `PDFPluginEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
