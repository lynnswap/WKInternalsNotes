# ``WKInternalsNotes/WKPreferences/_updateSceneGeometryEnabled``

Update Scene Geometry を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setUpdateSceneGeometryEnabled:) BOOL _updateSceneGeometryEnabled WK_API_AVAILABLE(visionos(WK_XROS_TBA));
```

## Default Value
visionOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_updateSceneGeometryEnabled = YES`: Update Scene Geometry を有効化する。
- `_updateSceneGeometryEnabled = NO`: Update Scene Geometry を無効化する。
- Implementation: [`Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2016`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2016) の `WebKit::resizeScene` が `updateSceneGeometryEnabled()` を参照する。

## Details
- WebPreferences key: `UpdateSceneGeometryEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm)
- [`Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml) (key: `UpdateSceneGeometryEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
