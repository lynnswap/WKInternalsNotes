# ``WKInternalsNotes/WKWebExtension/initWithManifestDictionary(_:resources:)``

manifest 辞書と resources 辞書から Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithManifestDictionary:(NSDictionary<NSString *, id> *)manifest resources:(nullable NSDictionary<NSString *, id> *)resources NS_DESIGNATED_INITIALIZER;
```

## Discussion
`manifest` の型を検証したうえで `[super init]` し、`API::Object::constructInWrapper<WebKit::WebExtension>` に `manifest` と `WebKit::toDataMap(resources)` を渡して内部オブジェクトを構築する。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil` を返す。

## References
- [`WKWebExtensionPrivate.h#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L82)
- [`WKWebExtension.mm#L167`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L167)
- [`WKWebExtension.mm#L423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
