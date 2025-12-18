# ``WKInternalsNotes/WKPreferences/_textAreasAreResizable``

Text Areas Are Resizable を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTextAreasAreResizable:) BOOL _textAreasAreResizable WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_textAreasAreResizable = YES`: Text Areas Are Resizable を有効化する。
- `_textAreasAreResizable = NO`: Text Areas Are Resizable を無効化する。
- Implementation: [[[`Source/WebCore/style/values/ui/StyleResize.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/values/ui/StyleResize.cpp)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/values/ui/StyleResize.cpp)](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/values/ui/StyleResize.cpp) で `textAreasAreResizable()` が参照される。

## Details
- WebPreferences key: `TextAreasAreResizable`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L236)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1299`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1299)
- [`Source/WebCore/style/values/ui/StyleResize.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/style/values/ui/StyleResize.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7851`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7851) (key: `TextAreasAreResizable`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
