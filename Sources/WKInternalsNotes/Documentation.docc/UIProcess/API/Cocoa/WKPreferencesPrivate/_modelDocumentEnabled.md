# ``WKInternalsNotes/WKPreferencesPrivate/_modelDocumentEnabled``

HTML <model> element for model documents を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setModelDocumentEnabled:) BOOL _modelDocumentEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_modelDocumentEnabled = YES`: HTML <model> element for model documents を有効化する。
- `_modelDocumentEnabled = NO`: HTML <model> element for model documents を無効化する。
- Implementation: [`Source/WebCore/page/DeprecatedGlobalSettings.h#L121`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L121) で `modelDocumentEnabled()` が参照される。

## Details
- WebPreferences key: `ModelDocumentEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L185)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1570`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1570)
- [`Source/WebCore/page/DeprecatedGlobalSettings.h#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/DeprecatedGlobalSettings.h#L120)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5365`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L5365) (key: `ModelDocumentEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
