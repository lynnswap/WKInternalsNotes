# ``WKInternalsNotes/_WKInspectorExtensionHost/showExtensionTabWithIdentifier(_:completionHandler:)``

Inspector 拡張タブを表示する。

## Objective-C Declaration
```objective-c
- (void)showExtensionTabWithIdentifier:(NSString *)extensionTabIdentifier completionHandler:(void(^)(NSError * _Nullable))completionHandler;
```

## Discussion
`extensionController` が無い場合は `InvalidRequest` をエラーとして返す。存在する場合は `showExtensionTab` を呼び、結果に応じて `NSError` または `nil` を返す。

## References
- [`_WKInspectorExtensionHost.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionHost.h#L64)
- [`_WKInspector.mm#L286`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L286)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
