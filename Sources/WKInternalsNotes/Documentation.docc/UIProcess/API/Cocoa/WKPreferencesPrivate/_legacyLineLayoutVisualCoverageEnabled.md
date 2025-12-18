# ``WKInternalsNotes/WKPreferences/_legacyLineLayoutVisualCoverageEnabled``

legacy line layout visual coverage を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLegacyLineLayoutVisualCoverageEnabled:) BOOL _legacyLineLayoutVisualCoverageEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_legacyLineLayoutVisualCoverageEnabled = YES`: legacy line layout visual coverage を有効化する。
- `_legacyLineLayoutVisualCoverageEnabled = NO`: legacy line layout visual coverage を無効化する。
- Implementation: [`RenderBlock.cpp#L1075`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBlock.cpp#L1075) の `RenderBlock::paintDebugBoxShadowIfApplicable` が `legacyLineLayoutVisualCoverageEnabled()` を参照する。

## Details
- WebPreferences key: `LegacyLineLayoutVisualCoverageEnabled`

## References
- [`WKPreferencesPrivate.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L80)
- [`WKPreferences.mm#L366`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L366)
- [`RenderBlock.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/rendering/RenderBlock.cpp)
- [`UnifiedWebPreferences.yaml#L4369`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4369) (key: `LegacyLineLayoutVisualCoverageEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
