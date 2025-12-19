# ``WKInternalsNotes/WKWebViewContentProviderRegistry/initWithConfiguration(_:)``

`WKWebViewConfiguration` に基づいて registry を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithConfiguration:(WKWebViewConfiguration *)configuration;
```

## Discussion
`USE(SYSTEM_PREVIEW)` かつ `configuration._systemPreviewEnabled` が有効で、`configuration.preferences._modelDocumentEnabled` が無効な場合に USD MIME type 向けの `WKUSDPreviewView` を登録する。

## References
- [`WKWebViewContentProviderRegistry.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.h#L37)
- [`WKWebViewContentProviderRegistry.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/WKWebViewContentProviderRegistry.mm#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
