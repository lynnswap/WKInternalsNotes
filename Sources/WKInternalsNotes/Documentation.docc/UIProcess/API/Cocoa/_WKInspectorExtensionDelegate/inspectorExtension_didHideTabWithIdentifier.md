# ``WKInternalsNotes/_WKInspectorExtensionDelegate/inspectorExtension(_:didHideTabWithIdentifier:)``

拡張タブが非表示になったことを通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorExtension:(_WKInspectorExtension *)extension didHideTabWithIdentifier:(NSString *)tabIdentifier;
```

## Discussion
`InspectorExtensionDelegate` が selector の有無と delegate の存在を確認し、条件を満たす場合に呼び出す。

## References
- [`InspectorExtensionDelegate.mm#L85`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/Cocoa/InspectorExtensionDelegate.mm#L85)
- [`_WKInspectorExtensionDelegate.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionDelegate.h#L54)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
