# ``WKInternalsNotes/WKWebExtension/initWithAppExtensionBundle(_:error:)``

アプリ拡張バンドルで Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithAppExtensionBundle:(NSBundle *)appExtensionBundle error:(NSError **)error NS_REFINED_FOR_SWIFT;
```

## Discussion
`initWithAppExtensionBundle:resourceBaseURL:error:` を `resourceBaseURL` に `nil` を渡して呼び出す。

## References
- [`WKWebExtensionPrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L32)
- [`WKWebExtension.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
