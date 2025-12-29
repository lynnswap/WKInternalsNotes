# ``WKInternalsNotes/_WKInspectorExtensionDelegate/inspectorExtension(_:didNavigateTabWithIdentifier:newURL:)``

拡張タブが新しい URL に遷移したことを通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorExtension:(_WKInspectorExtension *)extension didNavigateTabWithIdentifier:(NSString *)tabIdentifier newURL:(NSURL *)newURL;
```

## Discussion
`InspectorExtensionDelegate` が selector の有無と delegate の存在を確認し、条件を満たす場合に呼び出す。`newURL` は `WTF::URL` から `NSURL` に変換される。

## References
- [`InspectorExtensionDelegate.mm#L97`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/Cocoa/InspectorExtensionDelegate.mm#L97)
- [`_WKInspectorExtensionDelegate.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionDelegate.h#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
