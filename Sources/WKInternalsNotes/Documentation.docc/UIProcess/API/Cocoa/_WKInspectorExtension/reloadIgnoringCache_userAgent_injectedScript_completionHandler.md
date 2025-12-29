# ``WKInternalsNotes/_WKInspectorExtension/reloadIgnoringCache(_:userAgent:injectedScript:completionHandler:)``

検査対象ページのリロードを行う。

## Objective-C Declaration
```objective-c
- (void)reloadIgnoringCache:(BOOL)ignoreCache userAgent:(NSString *)userAgent injectedScript:(NSString *)injectedScript completionHandler:(void(^)(NSError * _Nullable))completionHandler;
```

## Discussion
`userAgent` と `injectedScript` は optional に変換して渡す。失敗時は `WKErrorDomain`/`WKErrorUnknown` の `NSError` を返し、成功時は `nil` を返す。

## References
- [`_WKInspectorExtension.h#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L93)
- [`_WKInspectorExtension.mm#L140`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L140)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
