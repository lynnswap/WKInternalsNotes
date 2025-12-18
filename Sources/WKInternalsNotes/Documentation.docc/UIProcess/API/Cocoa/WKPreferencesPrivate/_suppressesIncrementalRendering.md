# ``WKInternalsNotes/WKPreferences/_suppressesIncrementalRendering``

Incremental Rendering を抑制するかどうかを切り替える API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setSuppressesIncrementalRendering:) BOOL _suppressesIncrementalRendering WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_suppressesIncrementalRendering = YES`: Incremental Rendering を抑制する。
- `_suppressesIncrementalRendering = NO`: Incremental Rendering を抑制しない。
- Implementation: [`Source/WebCore/dom/Document.cpp#L2107`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp#L2107) の `Document::setVisualUpdatesAllowed` が `suppressesIncrementalRendering()` を参照する。

## Details
- WebPreferences key: `SuppressesIncrementalRendering`
- Candidate Public API: `WKWebViewConfiguration.suppressesIncrementalRendering`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L219)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1119)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)
- [`Source/WebCore/dom/Document.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/dom/Document.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7731`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7731) (key: `SuppressesIncrementalRendering`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
