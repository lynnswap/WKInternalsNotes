# ``WKInternalsNotes/WKPreferences/_fileSystemAccessEnabled``

File System API を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setFileSystemAccessEnabled:) BOOL _fileSystemAccessEnabled WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_fileSystemAccessEnabled = YES`: File System API を有効化する。
- `_fileSystemAccessEnabled = NO`: File System API を無効化する。
- Implementation: [`Source/WebCore/Modules/filesystem/FileSystemDirectoryHandle.idl#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/filesystem/FileSystemDirectoryHandle.idl#L39)（`EnabledBySetting=FileSystemEnabled`）

## Details
- WebPreferences key: `FileSystemEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L179)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1505`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1505)
- [`Source/WebCore/Modules/filesystem/FileSystemDirectoryHandle.idl`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/Modules/filesystem/FileSystemDirectoryHandle.idl)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2940`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2940) (key: `FileSystemEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
