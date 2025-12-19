# ``WKInternalsNotes/WKWebExtension/_hasModularBackgroundContent``

バックグラウンドコンテンツがモジュール形式かどうかを示す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) BOOL _hasModularBackgroundContent;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。有効時は `backgroundContentUsesModules()` の結果に依存する。

## Discussion
`ENABLE(WK_WEB_EXTENSIONS)` の場合は `_protectedWebExtension->backgroundContentUsesModules()` を返し、無効時は `NO`。

## References
- [`WKWebExtensionPrivate.h#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L97)
- [`WKWebExtension.mm#L325`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L325)
- [`WKWebExtension.mm#L325`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L325)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
