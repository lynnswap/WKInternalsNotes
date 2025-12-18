# ``WKInternalsNotes/WKWebExtension/_initWithResources(_:)``

resources 辞書だけで Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)_initWithResources:(NSDictionary<NSString *, id> *)resources NS_SWIFT_UNAVAILABLE("Use init(resources:).");
```

## Discussion
`initWithResources:` に委譲する。

## References
- [`WKWebExtensionPrivate.h#L37`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L37)
- [`WKWebExtension.mm#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L115)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
