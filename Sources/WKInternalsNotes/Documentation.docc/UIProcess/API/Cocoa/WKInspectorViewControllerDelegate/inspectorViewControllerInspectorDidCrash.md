# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewControllerInspectorDidCrash(_:)``

Inspector がクラッシュした通知を受ける。

## Objective-C Declaration
```objective-c
- (void)inspectorViewControllerInspectorDidCrash:(WKInspectorViewController *)inspectorViewController;
```

## Discussion
`WebInspectorUIProxy` を保持している場合に `closeForCrash()` を呼ぶ。

## References
- [`WKInspectorViewController.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L58)
- [`WebInspectorUIProxyMac.mm#L193`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L193)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
