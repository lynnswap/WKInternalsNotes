# ``WKInternalsNotes/WKPreferencesPrivate/_interactionRegionInlinePadding``

Interaction Region Inline Padding を設定する API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setInteractionRegionInlinePadding:) double _interactionRegionInlinePadding WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
iOS: `4` / macOS: `4`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_interactionRegionInlinePadding` を設定すると: Interaction Region Inline Padding を設定する。
- 既定値に戻すと: 既定の挙動に戻る。
- Implementation: [`Source/WebCore/page/InteractionRegion.cpp#L682`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/InteractionRegion.cpp#L682) の `RenderThemeCocoa::inflateRectForInteractionRegion` が `interactionRegionInlinePadding()` を参照する。

## Details
- WebPreferences key: `InteractionRegionInlinePadding`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L187)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1600`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1600)
- [`Source/WebCore/page/InteractionRegion.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/InteractionRegion.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3969`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L3969) (key: `InteractionRegionInlinePadding`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
