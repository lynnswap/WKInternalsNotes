# ``WKInternalsNotes/WKWebExtension/_initWithAppExtensionBundle(_:resourceBaseURL:error:)``

アプリ拡張バンドルとリソース基底 URL を指定して Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)_initWithAppExtensionBundle:(NSBundle *)appExtensionBundle resourceBaseURL:(NSURL *)resourceBaseURL error:(NSError **)error NS_SWIFT_UNAVAILABLE("Use init(appExtensionBundle:resourceBaseURL:).");
```

## Discussion
`initWithAppExtensionBundle:resourceBaseURL:error:` をそのまま呼び出す薄いラッパー。

## References
- [`WKWebExtensionPrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L34)
- [`WKWebExtension.mm#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L100)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
