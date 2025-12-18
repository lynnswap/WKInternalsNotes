# ``WKInternalsNotes/WKPreferences/_aggressiveTileRetentionEnabled``

Aggressive Tile Retention を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAggressiveTileRetentionEnabled:) BOOL _aggressiveTileRetentionEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_aggressiveTileRetentionEnabled = YES`: Aggressive Tile Retention を有効化する。
- `_aggressiveTileRetentionEnabled = NO`: Aggressive Tile Retention を無効化する。
- Implementation: [`Source/WebCore/rendering/RenderLayerBacking.cpp#L4310`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp#L4310) の `RenderLayerBacking::shouldAggressivelyRetainTiles` が `aggressiveTileRetentionEnabled()` を参照する。

## Details
- WebPreferences key: `AggressiveTileRetentionEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L239`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L239)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1329`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1329)
- [`Source/WebCore/rendering/RenderLayerBacking.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderLayerBacking.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L202`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L202) (key: `AggressiveTileRetentionEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
