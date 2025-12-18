# ``WKInternalsNotes/WKPreferences/_compositingBordersVisible``

Compositing borders visible を表示/非表示にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCompositingBordersVisible:) BOOL _compositingBordersVisible;
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_compositingBordersVisible = YES`: `GraphicsLayer` の `setShowDebugBorder(true)` が反映され、debug border が表示される。
- `_compositingBordersVisible = NO`: `GraphicsLayer` の `setShowDebugBorder(false)` が反映され、debug border が表示されない。
- Implementation: [`Source/WebCore/page/PageOverlayController.cpp#L352`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/PageOverlayController.cpp#L352) の `PageOverlayController::updateSettingsForLayer` が `settings->showDebugBorders()` を `layer.setShowDebugBorder(...)` に反映する。

## Details
- WebPreferences key: `CompositingBordersVisible`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L75)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L316`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L316)
- [`Source/WebCore/page/PageOverlayController.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/PageOverlayController.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1856`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1856) (key: `CompositingBordersVisible`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
