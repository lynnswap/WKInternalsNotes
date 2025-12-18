# ``WKInternalsNotes/WKPreferences/_acceleratedCompositingEnabled``

Accelerated Compositing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAcceleratedCompositingEnabled:) BOOL _acceleratedCompositingEnabled WK_API_AVAILABLE(macos(10.13.4), ios(13.4));
```

## Default Value
iOS: `YES` / macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_acceleratedCompositingEnabled = YES`: Accelerated Compositing を有効化する。
- `_acceleratedCompositingEnabled = NO`: Accelerated Compositing を無効化する。
- Implementation: [`HTMLCanvasElement.cpp#L341`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLCanvasElement.cpp#L341) の `HTMLCanvasElement::is2dType` が `acceleratedCompositingEnabled()` を参照する。

## Details
- WebPreferences key: `AcceleratedCompositingEnabled`

## References
- [`WKPreferencesPrivate.h#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L169)
- [`WKPreferences.mm#L978`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L978)
- [`HTMLCanvasElement.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/HTMLCanvasElement.cpp)
- [`UnifiedWebPreferences.yaml#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L99) (key: `AcceleratedCompositingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
