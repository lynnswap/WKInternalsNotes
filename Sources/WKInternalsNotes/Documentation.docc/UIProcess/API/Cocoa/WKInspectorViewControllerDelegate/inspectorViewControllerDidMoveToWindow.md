# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewControllerDidMoveToWindow(_:)``

Inspector のウィンドウ移動後に通知される。

## Objective-C Declaration
```objective-c
- (void)inspectorViewControllerDidMoveToWindow:(WKInspectorViewController *)inspectorViewController;
```

## Discussion
`WebInspectorUIProxy` を保持している場合に `attachmentDidMoveToWindow(inspectorViewController.webView.window)` を呼ぶ。

## References
- [`WKInspectorViewController.h#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L62)
- [`WebInspectorUIProxyMac.mm#L227`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L227)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
