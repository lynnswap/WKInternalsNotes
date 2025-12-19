# ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessIdentifier()``

NetworkProcess の PID を取得する。

## Objective-C Declaration
```objective-c
- (pid_t)_networkProcessIdentifier WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`networkProcess().processID()` を返す。

## References
- [`WKWebsiteDataStorePrivate.h#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L122)
- [`WKWebsiteDataStore.mm#L1226`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1226)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
