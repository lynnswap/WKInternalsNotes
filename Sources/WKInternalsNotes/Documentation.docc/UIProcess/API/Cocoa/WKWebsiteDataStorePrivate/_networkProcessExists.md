# ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessExists()``

`NetworkProcess` の存在を確認する。

## Objective-C Declaration
```objective-c
- (BOOL)_networkProcessExists WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`networkProcessIfExists()` の有無を `BOOL` で返す。

## References
- [`WKWebsiteDataStorePrivate.h#L124`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L124)
- [`WKWebsiteDataStore.mm#L1247`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1247)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
