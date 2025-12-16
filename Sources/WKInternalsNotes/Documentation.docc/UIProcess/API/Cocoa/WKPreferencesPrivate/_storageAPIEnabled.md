# ``WKInternalsNotes/WKPreferencesPrivate/_storageAPIEnabled``

Storage API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setStorageAPIEnabled:) BOOL _storageAPIEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_storageAPIEnabled = YES`: Storage API を有効化する。
- `_storageAPIEnabled = NO`: Storage API を無効化する。
- Implementation: [`Source/WebCore/Modules/storage/StorageManager.idl#L29`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/storage/StorageManager.idl#L29)（`EnabledBySetting=StorageAPIEnabled`）

## Details
- WebPreferences key: `StorageAPIEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L180)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1515`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1515)
- [`Source/WebCore/Modules/storage/StorageManager.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/storage/StorageManager.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7639`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L7639) (key: `StorageAPIEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
