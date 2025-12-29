# ``WKInternalsNotes/_WKInspectorExtension/createTabWithName(_:tabIconURL:sourceURL:completionHandler:)``

拡張用のタブを作成する。

## Objective-C Declaration
```objective-c
- (void)createTabWithName:(NSString *)tabName tabIconURL:(NSURL *)tabIconURL sourceURL:(NSURL *)sourceURL completionHandler:(void(^)(NSError * _Nullable, NSString * _Nullable inspectorTabIdentifier))completionHandler;
```

## Discussion
`InspectorExtension::createTab` を呼び、成功時はタブ識別子を返す。失敗時は `WKErrorDomain`/`WKErrorUnknown` の `NSError` を生成し、`NSLocalizedFailureReasonErrorKey` にエラー文字列を入れて返す。

## References
- [`_WKInspectorExtension.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.h#L53)
- [`_WKInspectorExtension.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtension.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
