# ``WKInternalsNotes/WKWebExtension/_hasServiceWorkerBackgroundContent``

バックグラウンドコンテンツがサービスワーカーかどうかを示す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) BOOL _hasServiceWorkerBackgroundContent;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。有効時は内部 WebExtension の `backgroundContentIsServiceWorker()` に依存する。

## Discussion
`ENABLE(WK_WEB_EXTENSIONS)` の場合は `_protectedWebExtension->backgroundContentIsServiceWorker()` を返し、無効時は `NO`。

## References
- [`WKWebExtensionPrivate.h#L94`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L94)
- [`WKWebExtension.mm#L320`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L320)
- [`WKWebExtension.mm#L558`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L558)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
