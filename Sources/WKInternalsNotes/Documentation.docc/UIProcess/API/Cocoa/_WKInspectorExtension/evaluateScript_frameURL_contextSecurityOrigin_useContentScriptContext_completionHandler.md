# ``WKInternalsNotes/_WKInspectorExtension/evaluateScript(_:frameURL:contextSecurityOrigin:useContentScriptContext:completionHandler:)``

検査対象ページのコンテキストで JavaScript を評価する。

## Objective-C Declaration
```objective-c
- (void)evaluateScript:(NSString *)scriptSource frameURL:(NSURL * _Nullable)frameURL contextSecurityOrigin:(NSURL * _Nullable)contextSecurityOrigin useContentScriptContext:(BOOL)useContentScriptContext completionHandler:(void(^)(NSError * _Nullable, id result))completionHandler;
```

## Discussion
`frameURL` と `contextSecurityOrigin` は `URL` の optional に変換される。評価結果がエラーなら `WKErrorDomain`/`WKErrorUnknown` の `NSError` を返し、例外なら `ExceptionDetails` 由来の `NSError` を返す。成功時は評価結果の `id` を返す。

## References
- [`_WKInspectorExtension.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L66)
- [`_WKInspectorExtension.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
