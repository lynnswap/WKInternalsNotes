# ``WKInternalsNotes/WKPreferences/_tiledScrollingIndicatorVisible``

Tiled scrolling indicator を表示/非表示にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTiledScrollingIndicatorVisible:) BOOL _tiledScrollingIndicatorVisible;
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_tiledScrollingIndicatorVisible = YES`: Tiled scrolling indicator を表示する。
- `_tiledScrollingIndicatorVisible = NO`: Tiled scrolling indicator を非表示にする。
- Implementation: [`Source/WebKit/UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.mm#L102) の `IOSurfacePool::sharedPoolSingleton` が `tiledScrollingIndicatorVisible()` を参照する。

## Details
- WebPreferences key: `TiledScrollingIndicatorVisible`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L77)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L336`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L336)
- [`Source/WebKit/UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/RemoteLayerTreeDrawingAreaProxy.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8032`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8032) (key: `TiledScrollingIndicatorVisible`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
