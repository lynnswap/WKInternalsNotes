# ``WKInternalsNotes/WKPreferences/_compositingRepaintCountersVisible``

Compositing repaint counters visible を表示/非表示にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setCompositingRepaintCountersVisible:) BOOL _compositingRepaintCountersVisible;
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_compositingRepaintCountersVisible = YES`: `GraphicsLayer` の `setShowRepaintCounter(true)` が反映され、repaint counter が表示される。
- `_compositingRepaintCountersVisible = NO`: `GraphicsLayer` の `setShowRepaintCounter(false)` が反映され、repaint counter が表示されない。
- Implementation: [`PageOverlayController.cpp#L352`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/PageOverlayController.cpp#L352) の `PageOverlayController::updateSettingsForLayer` が `settings->showRepaintCounter()` を `layer.setShowRepaintCounter(...)` に反映する。

## Details
- WebPreferences key: `CompositingRepaintCountersVisible`

## References
- [`WKPreferencesPrivate.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L76)
- [`WKPreferences.mm#L326`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L326)
- [`PageOverlayController.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/PageOverlayController.cpp)
- [`UnifiedWebPreferences.yaml#L1874`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L1874) (key: `CompositingRepaintCountersVisible`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
