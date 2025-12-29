# ``WKInternalsNotes/WKInspectorResourceURLSchemeHandler/allowedURLSchemesForCSP``

Inspector の CSP に許可する URL スキームの集合。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSSet<NSString *> *allowedURLSchemesForCSP;
```

## Default Value
`nil`。

## Discussion
getter は保持している `NSSet` を返し、setter は渡された集合を `copy` して保持する。`startURLSchemeTask:` でメインの Inspector リソース URL の場合に、この集合を元に `Content-Security-Policy` の `connect-src` と `img-src` の許可スキームを生成する。

## References
- [`WKInspectorResourceURLSchemeHandler.mm#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorResourceURLSchemeHandler.mm#L47)
- [`WKInspectorResourceURLSchemeHandler.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorResourceURLSchemeHandler.mm#L113)
- [`WKInspectorResourceURLSchemeHandler.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorResourceURLSchemeHandler.h#L36)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
