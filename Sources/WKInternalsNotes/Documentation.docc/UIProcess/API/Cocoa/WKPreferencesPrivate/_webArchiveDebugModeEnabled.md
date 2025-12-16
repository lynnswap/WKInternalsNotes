# ``WKInternalsNotes/WKPreferencesPrivate/_webArchiveDebugModeEnabled``

web archive debug mode を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setWebArchiveDebugModeEnabled:) BOOL _webArchiveDebugModeEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_webArchiveDebugModeEnabled = YES`: web archive debug mode を有効化する。
- `_webArchiveDebugModeEnabled = NO`: web archive debug mode を無効化する。
- Implementation: [`Source/WebCore/loader/DocumentLoader.cpp#L1848`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/DocumentLoader.cpp#L1848) の `DocumentLoader::scheduleArchiveLoad` が `webArchiveDebugModeEnabled()` を参照する。

## Details
- WebPreferences key: `WebArchiveDebugModeEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L212)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1049`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1049)
- [`Source/WebCore/loader/DocumentLoader.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/DocumentLoader.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8887`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L8887) (key: `WebArchiveDebugModeEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
