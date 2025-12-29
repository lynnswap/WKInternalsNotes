# ``WKInternalsNotes/_WKInspectorExtensionDelegate/inspectorExtension(_:inspectedPageDidNavigate:)``

被検査ページの遷移を通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorExtension:(_WKInspectorExtension *)extension inspectedPageDidNavigate:(NSURL *)url;
```

## Discussion
`InspectorExtensionDelegate` が selector の有無と delegate の存在を確認し、条件を満たす場合に呼び出す。`url` は `WTF::URL` から `NSURL` に変換される。

## References
- [`InspectorExtensionDelegate.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/Cocoa/InspectorExtensionDelegate.mm#L109)
- [`_WKInspectorExtensionDelegate.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionDelegate.h#L69)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
