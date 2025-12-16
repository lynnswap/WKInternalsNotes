# ``WKInternalsNotes/WKPreferencesPrivate/_serviceControlsEnabled``

Service Controls を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setServiceControlsEnabled:) BOOL _serviceControlsEnabled WK_API_AVAILABLE(macos(10.14));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_serviceControlsEnabled = YES`: Service Controls を有効化する。
- `_serviceControlsEnabled = NO`: Service Controls を無効化する。
- Implementation: [`Source/WebCore/page/mac/ServicesOverlayController.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/mac/ServicesOverlayController.mm#L243) の `ServicesOverlayController::invalidateHighlightsOfType` が `serviceControlsEnabled()` を参照する。

## Details
- WebPreferences key: `ServiceControlsEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L234`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L234)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1279`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1279)
- [`Source/WebCore/page/mac/ServicesOverlayController.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/mac/ServicesOverlayController.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6951`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L6951) (key: `ServiceControlsEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
