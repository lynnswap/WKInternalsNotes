# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/closeFromFrontend()``

フロントエンドからの close を delegate に通知する。

## Objective-C Declaration
```objective-c
- (void)closeFromFrontend;
```

## Discussion
- RemoteWebInspectorUIProxyClient 経由で呼ばれ、delegate が `inspectorViewControllerInspectorDidClose:` を実装している場合に通知する。
- delegate が未設定 / 未実装の場合は no-op。

## References
- [`_WKRemoteWebInspectorViewController.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h)
- [`_WKRemoteWebInspectorViewController.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L52)
- [`_WKRemoteWebInspectorViewController.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
