# ``WKInternalsNotes/_WKInspectorExtensionHost/navigateExtensionTabWithIdentifier(_:toURL:completionHandler:)``

拡張タブの URL を指定して読み込ませる。

## Objective-C Declaration
```objective-c
- (void)navigateExtensionTabWithIdentifier:(NSString *)extensionTabIdentifier toURL:(NSURL *)url completionHandler:(void(^)(NSError * _Nullable))completionHandler;
```

## Discussion
`extensionController` が無い場合は `InvalidRequest` をエラーとして返す。存在する場合は `navigateTabForExtension` を呼び、結果に応じて `NSError` または `nil` を返す。

## References
- [`_WKInspectorExtensionHost.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionHost.h#L74)
- [`_WKInspector.mm#L306`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L306)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
