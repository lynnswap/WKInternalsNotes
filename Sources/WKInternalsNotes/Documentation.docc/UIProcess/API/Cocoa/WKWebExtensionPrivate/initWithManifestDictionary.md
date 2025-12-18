# ``WKInternalsNotes/WKWebExtension/initWithManifestDictionary(_:)``

manifest 辞書から Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithManifestDictionary:(NSDictionary<NSString *, id> *)manifest;
```

## Discussion
`manifest` が `NSDictionary` であることを `NSParameterAssert` し、`initWithManifestDictionary:resources:` に `resources` を `nil` で渡して委譲する。

## References
- [`WKWebExtensionPrivate.h#L72`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L72)
- [`WKWebExtension.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
