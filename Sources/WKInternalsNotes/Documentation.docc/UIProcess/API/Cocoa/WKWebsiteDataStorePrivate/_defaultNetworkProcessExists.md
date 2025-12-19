# ``WKInternalsNotes/WKWebsiteDataStore/_defaultNetworkProcessExists()``

デフォルトの `NetworkProcess` の存在を確認する。

## Objective-C Declaration
```objective-c
+ (BOOL)_defaultNetworkProcessExists WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`NetworkProcessProxy::defaultNetworkProcess()` の有無を `BOOL` で返す。

## References
- [`WKWebsiteDataStorePrivate.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L125)
- [`WKWebsiteDataStore.mm#L1252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1252)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
