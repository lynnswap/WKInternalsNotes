# ``WKInternalsNotes/WKPreferencesPrivate/_textAutosizingEnabled``

Text Autosizing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setTextAutosizingEnabled:) BOOL _textAutosizingEnabled WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
iOS: `YES` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_textAutosizingEnabled = YES`: Text Autosizing を有効化する。
- `_textAutosizingEnabled = NO`: Text Autosizing を無効化する。
- Implementation: [`Source/WebCore/page/LocalFrameViewLayoutContext.cpp#L617`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/LocalFrameViewLayoutContext.cpp#L617) の `LocalFrameViewLayoutContext::applyTextSizingIfNeeded` が `textAutosizingEnabled()` を参照する。

## Details
- WebPreferences key: `TextAutosizingEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L86)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L426`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L426)
- [`Source/WebCore/page/LocalFrameViewLayoutContext.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/LocalFrameViewLayoutContext.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7864`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7864) (key: `TextAutosizingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
