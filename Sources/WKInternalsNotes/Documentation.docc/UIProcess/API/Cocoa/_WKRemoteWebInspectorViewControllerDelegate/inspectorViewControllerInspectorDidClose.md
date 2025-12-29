# ``WKInternalsNotes/_WKRemoteWebInspectorViewControllerDelegate/inspectorViewControllerInspectorDidClose(_:)``

インスペクタが閉じられたことを通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorViewControllerInspectorDidClose:(_WKRemoteWebInspectorViewController *)controller;
```

## Discussion
フロントエンドからの close 要求で `closeFromFrontend` が呼ばれた際に、`respondsToSelector:` を確認してデリゲートへ通知する。

## References
- [`_WKRemoteWebInspectorViewController.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L59)
- [`_WKRemoteWebInspectorViewController.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
