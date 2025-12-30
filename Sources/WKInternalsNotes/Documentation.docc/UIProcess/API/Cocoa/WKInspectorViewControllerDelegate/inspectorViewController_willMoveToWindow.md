# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewController(_:willMoveToWindow:)``

Inspector のウィンドウ移動前に通知される。

## Objective-C Declaration
```objective-c
- (void)inspectorViewController:(WKInspectorViewController *)inspectorViewController willMoveToWindow:(NSWindow *)newWindow;
```

## Discussion
`WebInspectorUIProxy` を保持している場合に `attachmentWillMoveFromWindow(inspectorViewController.webView.window)` を呼ぶ。

## References
- [`WKInspectorViewController.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L61)
- [`WebInspectorUIProxyMac.mm#L221`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L221)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
