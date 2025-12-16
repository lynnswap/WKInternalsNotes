# ``WKInternalsNotes/WKPreferencesPrivate/_overlayRegionsEnabled``

Overlay Regions を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverlayRegionsEnabled:) BOOL _overlayRegionsEnabled WK_API_AVAILABLE(visionos(2.4));
```

## Default Value
visionOS: `NO`

## Details
- Public API: `WKPreferences.isLookToScrollEnabled`
- WebPreferences key: `OverlayRegionsEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L199)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1684`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1684)
- [`Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteScrollingCoordinatorProxyIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/RemoteLayerTree/ios/RemoteScrollingCoordinatorProxyIOS.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5747) (key: `OverlayRegionsEnabled`)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
