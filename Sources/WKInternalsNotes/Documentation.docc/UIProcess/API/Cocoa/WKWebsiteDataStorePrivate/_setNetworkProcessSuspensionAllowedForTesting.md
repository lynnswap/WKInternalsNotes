# ``WKInternalsNotes/WKWebsiteDataStore/_setNetworkProcessSuspensionAllowedForTesting(_:)``

テスト用に NetworkProcess のサスペンド許可を設定する。

## Objective-C Declaration
```objective-c
+ (void)_setNetworkProcessSuspensionAllowedForTesting:(BOOL)allowed WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`NetworkProcessProxy::setSuspensionAllowedForTesting` を呼ぶ。

## References
- [`WKWebsiteDataStorePrivate.h#L119`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L119)
- [`WKWebsiteDataStore.mm#L1236`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L1236)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
