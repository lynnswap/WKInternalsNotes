# ``WKInternalsNotes/WKWebsiteDataStore/_initWithConfiguration(_:)``

指定した構成でデータストアを初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)_initWithConfiguration:(_WKWebsiteDataStoreConfiguration *)configuration WK_API_AVAILABLE(macos(10.13), ios(11.0));
```

## Discussion
永続/非永続に応じた `SessionID` を生成し、`WebsiteDataStore` を構築してディレクトリ解決を開始する。

## References
- [`WKWebsiteDataStorePrivate.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h#L58)
- [`WKWebsiteDataStore.mm#L794`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStore.mm#L794)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
