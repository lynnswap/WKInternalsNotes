# ``WKInternalsNotes/WKPreferencesPrivate/_useGiantTiles``

Use giant tiles を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUseGiantTiles:) BOOL _useGiantTiles WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_useGiantTiles = YES`: Use giant tiles を有効化する。
- `_useGiantTiles = NO`: Use giant tiles を無効化する。
- Implementation: [`Source/WebCore/platform/graphics/GraphicsLayerClient.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/platform/graphics/GraphicsLayerClient.h#L131) で `useGiantTiles()` が参照される。

## Details
- WebPreferences key: `UseGiantTiles`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L237)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1309`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1309)
- [`Source/WebCore/platform/graphics/GraphicsLayerClient.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/platform/graphics/GraphicsLayerClient.h)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8355`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8355) (key: `UseGiantTiles`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
