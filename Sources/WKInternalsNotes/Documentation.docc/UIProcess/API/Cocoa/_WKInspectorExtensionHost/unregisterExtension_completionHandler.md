# ``WKInternalsNotes/_WKInspectorExtensionHost/unregisterExtension(_:completionHandler:)``

Inspector 拡張の登録解除を行う。

## Objective-C Declaration
```objective-c
- (void)unregisterExtension:(_WKInspectorExtension *)extension completionHandler:(void(^)(NSError * _Nullable))completionHandler;
```

## Discussion
`extensionController` が無い場合は `InvalidRequest` をエラーとして返す。存在する場合は `extension.extensionID` を使って `unregisterExtension` を呼び、結果に応じて `NSError` または `nil` を返す。

## References
- [`_WKInspectorExtensionHost.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionHost.h#L55)
- [`_WKInspector.mm#L264`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L264)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
