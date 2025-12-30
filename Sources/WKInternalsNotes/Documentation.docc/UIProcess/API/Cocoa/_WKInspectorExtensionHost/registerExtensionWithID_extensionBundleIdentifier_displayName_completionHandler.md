# ``WKInternalsNotes/_WKInspectorExtensionHost/registerExtensionWithID(_:extensionBundleIdentifier:displayName:completionHandler:)``

Inspector 拡張を登録する。

## Objective-C Declaration
```objective-c
- (void)registerExtensionWithID:(NSString *)extensionID extensionBundleIdentifier:(NSString *)extensionBundleIdentifier displayName:(NSString *)displayName completionHandler:(void(^)(NSError * _Nullable, _WKInspectorExtension * _Nullable))completionHandler;
```

## Discussion
`extensionController` が無い場合は `InvalidRequest` をエラーとして返す。存在する場合は `registerExtension` を呼び、結果に応じて `NSError` と `_WKInspectorExtension` を返す。

## References
- [`_WKInspectorExtensionHost.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionHost.h#L46)
- [`_WKInspector.mm#L242`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L242)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
