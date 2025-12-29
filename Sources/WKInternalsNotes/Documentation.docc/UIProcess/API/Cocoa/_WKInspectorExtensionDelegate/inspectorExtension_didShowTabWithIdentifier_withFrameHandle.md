# ``WKInternalsNotes/_WKInspectorExtensionDelegate/inspectorExtension(_:didShowTabWithIdentifier:withFrameHandle:)``

拡張タブが表示されたことを通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorExtension:(_WKInspectorExtension *)extension didShowTabWithIdentifier:(NSString *)tabIdentifier withFrameHandle:(_WKFrameHandle *)frameHandle;
```

## Discussion
`InspectorExtensionDelegate` が selector の有無を確認し、delegate が存在する場合に呼び出す。`frameHandle` は `FrameIdentifier` から生成した `API::FrameHandle` のラッパー。

## References
- [`InspectorExtensionDelegate.mm#L73`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/Cocoa/InspectorExtensionDelegate.mm#L73)
- [`_WKInspectorExtensionDelegate.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionDelegate.h#L47)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
