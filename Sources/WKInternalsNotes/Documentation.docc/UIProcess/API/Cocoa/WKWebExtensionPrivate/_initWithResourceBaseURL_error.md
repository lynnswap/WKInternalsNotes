# ``WKInternalsNotes/WKWebExtension/_initWithResourceBaseURL(_:error:)``

リソース基底 URL から Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)_initWithResourceBaseURL:(NSURL *)resourceBaseURL error:(NSError **)error NS_SWIFT_UNAVAILABLE("Use init(resourceBaseURL:).");
```

## Discussion
`initWithAppExtensionBundle:resourceBaseURL:error:` を `appExtensionBundle` に `nil` を渡して呼び出す。

## References
- [`WKWebExtensionPrivate.h#L33`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L33)
- [`WKWebExtension.mm#L95`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L95)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
