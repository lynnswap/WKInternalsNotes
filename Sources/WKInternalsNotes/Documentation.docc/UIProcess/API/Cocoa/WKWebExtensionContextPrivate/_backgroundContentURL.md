# ``WKInternalsNotes/WKWebExtensionContext/_backgroundContentURL``

拡張のバックグラウンドコンテンツ URL を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly) NSURL *_backgroundContentURL;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。有効時は `backgroundContentURL()` の結果（バックグラウンドコンテンツがない場合は `nil`）。

## Discussion
`_protectedWebExtensionContext->backgroundContentURL()` を `NSURL` に変換して返す。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。

## References
- [`WKWebExtensionContextPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContextPrivate.h#L38)
- [`WKWebExtensionContext.mm#L850`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L850)
- [`WKWebExtensionContext.mm#L850`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionContext.mm#L850)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
