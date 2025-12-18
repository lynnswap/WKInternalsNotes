# ``WKInternalsNotes/WKWebExtension/_initWithManifestDictionary(_:resources:)``

manifest 辞書と resources 辞書から Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)_initWithManifestDictionary:(NSDictionary<NSString *, id> *)manifest resources:(nullable NSDictionary<NSString *, id> *)resources NS_SWIFT_UNAVAILABLE("Use init(manifestDictionary:resources:).");
```

## Discussion
`initWithManifestDictionary:resources:` をそのまま呼び出す。

## References
- [`WKWebExtensionPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L36)
- [`WKWebExtension.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
