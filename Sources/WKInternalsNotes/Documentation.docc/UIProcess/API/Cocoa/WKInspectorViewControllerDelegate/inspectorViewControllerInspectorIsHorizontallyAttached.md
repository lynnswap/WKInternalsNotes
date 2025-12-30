# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewControllerInspectorIsHorizontallyAttached(_:)``

Inspector が横方向にアタッチされているかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)inspectorViewControllerInspectorIsHorizontallyAttached:(WKInspectorViewController *)inspectorViewController;
```

## Discussion
未アタッチなら `NO`。アタッチ済みの場合、`AttachmentSide` が `Left/Right` なら `YES`、`Bottom` なら `NO`。

## References
- [`WKInspectorViewController.h#L60`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L60)
- [`WebInspectorUIProxyMac.mm#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L204)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
