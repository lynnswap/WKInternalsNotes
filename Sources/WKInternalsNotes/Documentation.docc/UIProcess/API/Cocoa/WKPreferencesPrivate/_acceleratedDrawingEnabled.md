# ``WKInternalsNotes/WKPreferences/_acceleratedDrawingEnabled``

`GraphicsLayer` の accelerated drawing（Cocoa: `CALayer.drawsAsynchronously`）を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAcceleratedDrawingEnabled:) BOOL _acceleratedDrawingEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_acceleratedDrawingEnabled = YES`: `GraphicsLayer` の accelerated drawing を有効化する（Cocoa: `CALayer.drawsAsynchronously = YES`）。
- `_acceleratedDrawingEnabled = NO`: `GraphicsLayer` の accelerated drawing を無効化する（Cocoa: `CALayer.drawsAsynchronously = NO`）。ただし内容によっては個別に accelerated drawing が有効化される場合がある（例: Canvas の `shouldAccelerate`）。

## Details
- WebPreferences key: `AcceleratedDrawingEnabled`
- 反映先（Cocoa）: `PlatformCALayerCocoa::setAcceleratesDrawing` → `CALayer.drawsAsynchronously`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L82)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L386`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L386)
- [`Source/WebCore/page/PageOverlayController.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/PageOverlayController.cpp)
- [`Source/WebCore/rendering/RenderLayerBacking.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp)
- [`Source/WebCore/platform/graphics/ca/cocoa/PlatformCALayerCocoa.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/platform/graphics/ca/cocoa/PlatformCALayerCocoa.mm)
- [`Source/WebCore/svg/graphics/SVGImage.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/svg/graphics/SVGImage.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L124) (key: `AcceleratedDrawingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
