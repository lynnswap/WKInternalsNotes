# ``WKInternalsNotes/WKWebsiteDataStore/_configuration``

内部設定オブジェクトのコピーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) _WKWebsiteDataStoreConfiguration *_configuration;
```

## Default Value
初期化時に設定された configuration のコピー。

## Discussion
`_websiteDataStore->configuration()` を `copy()` してラップし返す。

## References
- [`WKWebsiteDataStorePrivate.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L111)
- [`WKWebsiteDataStore.mm#L800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L800)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
