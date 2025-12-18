# ``WKInternalsNotes/WKWebExtension/initWithResourceBaseURL(_:error:)``

リソース基底 URL で Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithResourceBaseURL:(NSURL *)resourceBaseURL error:(NSError **)error NS_REFINED_FOR_SWIFT;
```

## Discussion
`initWithAppExtensionBundle:resourceBaseURL:error:` を `appExtensionBundle` に `nil` を渡して呼び出す。

## References
- [`WKWebExtensionPrivate.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L54)
- [`WKWebExtension.mm#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L125)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
