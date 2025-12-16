# ``WKInternalsNotes/WKPreferencesPrivate/_canvasUsesAcceleratedDrawing``

Canvas uses accelerated drawing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCanvasUsesAcceleratedDrawing:) BOOL _canvasUsesAcceleratedDrawing WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_canvasUsesAcceleratedDrawing = YES`: `CanvasBase::shouldAccelerate` が `true` を返せるようになり、2D canvas の `RenderingMode::Accelerated` 選択経路が有効化される。
- `_canvasUsesAcceleratedDrawing = NO`: `CanvasBase::shouldAccelerate` が `false` を返し、2D canvas の `RenderingMode::Accelerated` が選択されない。
- Implementation: [`Source/WebCore/html/CanvasBase.cpp#L281`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/CanvasBase.cpp#L281) の `CanvasBase::shouldAccelerate` は `settingsValues().canvasUsesAcceleratedDrawing` が `false` の場合 `false` を返す。

## Details
- WebPreferences key: `CanvasUsesAcceleratedDrawing`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L208)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1009`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1009)
- [`Source/WebCore/html/CanvasBase.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/CanvasBase.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1706`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1706) (key: `CanvasUsesAcceleratedDrawing`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
