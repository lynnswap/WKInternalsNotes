# ``WKInternalsNotes/_WKInspectorExtension/navigateToURL(_:inTabWithIdentifier:completionHandler:)``

拡張タブを指定 URL に遷移させる。

## Objective-C Declaration
```objective-c
- (void)navigateToURL:(NSURL *)url inTabWithIdentifier:(NSString *)tabIdentifier completionHandler:(void(^)(NSError * _Nullable))completionHandler;
```

## Discussion
`navigateTab` を呼び、失敗時は `WKErrorDomain`/`WKErrorUnknown` の `NSError` を返す。成功時は `nil` を返す。

## References
- [`_WKInspectorExtension.h#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L84)
- [`_WKInspectorExtension.mm#L128`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L128)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
