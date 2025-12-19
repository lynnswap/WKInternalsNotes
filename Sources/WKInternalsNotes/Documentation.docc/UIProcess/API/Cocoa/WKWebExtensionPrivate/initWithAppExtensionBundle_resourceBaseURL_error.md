# ``WKInternalsNotes/WKWebExtension/initWithAppExtensionBundle(_:resourceBaseURL:error:)``

アプリ拡張バンドルまたはリソース基底 URL から Web 拡張を初期化する。

## Objective-C Declaration
```objective-c
- (nullable instancetype)initWithAppExtensionBundle:(nullable NSBundle *)appExtensionBundle resourceBaseURL:(nullable NSURL *)resourceBaseURL error:(NSError **)error NS_DESIGNATED_INITIALIZER;
```

## Discussion
bundle か URL のどちらかが必須であることを `NSParameterAssert` で検証し、`error` を `nil` に初期化したうえで `API::Object::constructInWrapper<WebKit::WebExtension>` で内部オブジェクトを構築する。内部エラーがあれば `NSError` を設定して `nil` を返す。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NSFeatureUnsupportedError` を設定して `nil` を返す。

## References
- [`WKWebExtensionPrivate.h#L32`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionPrivate.h#L32)
- [`WKWebExtension.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L90)
- [`WKWebExtension.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtension.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
