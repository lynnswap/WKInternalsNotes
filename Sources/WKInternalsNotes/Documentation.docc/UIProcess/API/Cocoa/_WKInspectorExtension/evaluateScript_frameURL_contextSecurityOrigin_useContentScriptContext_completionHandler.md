# ``WKInternalsNotes/_WKInspectorExtension/evaluateScript(_:frameURL:contextSecurityOrigin:useContentScriptContext:completionHandler:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)evaluateScript:(NSString *)scriptSource frameURL:(NSURL * _Nullable)frameURL contextSecurityOrigin:(NSURL * _Nullable)contextSecurityOrigin useContentScriptContext:(BOOL)useContentScriptContext completionHandler:(void(^)(NSError * _Nullable, id result))completionHandler;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`_WKInspectorExtension.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
