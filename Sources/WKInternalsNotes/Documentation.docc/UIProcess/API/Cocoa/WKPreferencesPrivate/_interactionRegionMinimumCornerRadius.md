# ``WKInternalsNotes/WKPreferences/_interactionRegionMinimumCornerRadius``

Interaction Region Minimum Corner Radius を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInteractionRegionMinimumCornerRadius:) double _interactionRegionMinimumCornerRadius WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
iOS: `8` / macOS: `8`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_interactionRegionMinimumCornerRadius` を設定すると: Interaction Region Minimum Corner Radius を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/rendering/RenderLayerBacking.cpp#L2134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp#L2134) の `RenderLayerBacking::updateEventRegion` が `interactionRegionMinimumCornerRadius()` を参照する。

## Details
- WebPreferences key: `InteractionRegionMinimumCornerRadius`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L186)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1590`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1590)
- [`Source/WebCore/rendering/RenderLayerBacking.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3980`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3980) (key: `InteractionRegionMinimumCornerRadius`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
