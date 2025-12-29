# ``WKInternalsNotes/_WKInspectorExtension/evaluateScript(_:inTabWithIdentifier:completionHandler:)``

拡張タブのコンテキストで JavaScript を評価する。

## Objective-C Declaration
```objective-c
- (void)evaluateScript:(NSString *)scriptSource inTabWithIdentifier:(NSString *)tabIdentifier completionHandler:(void(^)(NSError * _Nullable, id result))completionHandler;
```

## Discussion
`evaluateScriptInExtensionTab` を呼び、エラーなら `WKErrorDomain`/`WKErrorUnknown` の `NSError` を返す。例外時は `ExceptionDetails` 由来の `NSError` を返し、成功時は評価結果の `id` を返す。

## References
- [`_WKInspectorExtension.h#L76`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L76)
- [`_WKInspectorExtension.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
