# ``WKInternalsNotes/WKPreferencesPrivate/_webGLEnabled``

WebGL を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWebGLEnabled:) BOOL _webGLEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `YES`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_webGLEnabled = YES`: WebGL を有効化する。
- `_webGLEnabled = NO`: WebGL を無効化する。
- Implementation: [`Source/WebCore/html/canvas/WebGL2RenderingContext.idl#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/canvas/WebGL2RenderingContext.idl#L62)（`EnabledBySetting=WebGLEnabled`）

## Details
- WebPreferences key: `WebGLEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L207)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1169)
- [`Source/WebCore/html/canvas/WebGL2RenderingContext.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/html/canvas/WebGL2RenderingContext.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L9126`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L9126) (key: `WebGLEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
