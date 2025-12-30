# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewControllerDidBecomeActive(_:)``

Inspector がアクティブになった通知を受ける。

## Objective-C Declaration
```objective-c
- (void)inspectorViewControllerDidBecomeActive:(WKInspectorViewController *)inspectorViewController;
```

## Discussion
`WebInspectorUIProxy` を保持している場合に `didBecomeActive()` を呼ぶ。

## References
- [`WKInspectorViewController.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L57)
- [`WebInspectorUIProxyMac.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
