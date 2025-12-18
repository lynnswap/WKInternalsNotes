# ``WKInternalsNotes/WKPreferences/_accessHandleEnabled``

AccessHandle API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAccessHandleEnabled:) BOOL _accessHandleEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_accessHandleEnabled = YES`: AccessHandle API を有効化する。
- `_accessHandleEnabled = NO`: AccessHandle API を無効化する。
- Implementation: [`FileSystemFileHandle.idl#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/filesystem/FileSystemFileHandle.idl#L29)（`EnabledBySetting=AccessHandleEnabled`）

## Details
- WebPreferences key: `AccessHandleEnabled`

## References
- [`WKPreferencesPrivate.h#L181`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L181)
- [`WKPreferences.mm#L1525`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1525)
- [`FileSystemFileHandle.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/filesystem/FileSystemFileHandle.idl)
- [`UnifiedWebPreferences.yaml#L171`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L171) (key: `AccessHandleEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
