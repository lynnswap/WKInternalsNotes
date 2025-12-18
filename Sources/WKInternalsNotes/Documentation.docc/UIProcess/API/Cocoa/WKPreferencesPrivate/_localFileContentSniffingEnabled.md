# ``WKInternalsNotes/WKPreferences/_localFileContentSniffingEnabled``

Local File Content Sniffing を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setLocalFileContentSniffingEnabled:) BOOL _localFileContentSniffingEnabled WK_API_AVAILABLE(macos(10.13.4));
```

## Default Value
macOS: `NO`

## Discussion
- この API を使わない場合: 既定値のまま動作する。
- `_localFileContentSniffingEnabled = YES`: Local File Content Sniffing を有効化する。
- `_localFileContentSniffingEnabled = NO`: Local File Content Sniffing を無効化する。
- Implementation: [`EmptyClients.cpp#L247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/EmptyClients.cpp#L247) の `IDBClient::IDBConnectionToServer::create` が `localFileContentSniffingEnabled()` を参照する。

## Details
- WebPreferences key: `LocalFileContentSniffingEnabled`

## References
- [`WKPreferencesPrivate.h#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L213)
- [`WKPreferences.mm#L1059`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L1059)
- [`EmptyClients.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/loader/EmptyClients.cpp)
- [`UnifiedWebPreferences.yaml#L4580`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L4580) (key: `LocalFileContentSniffingEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
