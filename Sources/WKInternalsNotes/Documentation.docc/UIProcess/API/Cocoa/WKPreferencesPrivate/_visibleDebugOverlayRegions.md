# ``WKInternalsNotes/WKPreferences/_visibleDebugOverlayRegions``

Visible Debug Overlay Regions を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setVisibleDebugOverlayRegions:) _WKDebugOverlayRegions _visibleDebugOverlayRegions WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `0` / macOS: `0`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_visibleDebugOverlayRegions` を設定すると: Visible Debug Overlay Regions を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/rendering/RenderLayerBacking.cpp#L4037`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp#L4037) の `RenderLayerBacking::paintDebugOverlays` が `renderer().settings().visibleDebugOverlayRegions()` を参照して debug overlay を描画する。

## Details
- WebPreferences key: `VisibleDebugOverlayRegions`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L79`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L79)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L356`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L356)
- [`Source/WebCore/rendering/RenderLayerBacking.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8735`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8735) (key: `VisibleDebugOverlayRegions`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
