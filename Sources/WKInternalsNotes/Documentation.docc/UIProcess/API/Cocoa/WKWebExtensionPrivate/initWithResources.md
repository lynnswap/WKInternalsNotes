# ``WKInternalsNotes/WKWebExtension/initWithResources(_:)``

resources 辞書のみから Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithResources:(NSDictionary<NSString *, id> *)resources NS_DESIGNATED_INITIALIZER;
```

## Discussion
`resources` の型を検証したうえで `[super init]` し、`API::Object::constructInWrapper<WebKit::WebExtension>` に `WebKit::toDataMap(resources)` を渡して内部オブジェクトを構築する。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil` を返す。

## References
- [`WKWebExtensionPrivate.h#L91`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L91)
- [`WKWebExtension.mm#L179`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L179)
- [`WKWebExtension.mm#L428`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L428)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
