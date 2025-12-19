# ``WKInternalsNotes/WKWebsiteDataStore/_setPrivateTokenIPCForTesting(_:)``

テスト用に Private Token IPC を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateTokenIPCForTesting:(bool)enabled WK_API_AVAILABLE(macos(14.5), ios(17.5), visionos(1.2));
```

## Discussion
`setPrivateTokenIPCForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L108)
- [`WKWebsiteDataStore.mm#L1129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
