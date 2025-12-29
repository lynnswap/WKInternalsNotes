# ``WKInternalsNotes/_WKRemoteWebInspectorViewControllerDelegate/inspectorViewController(_:sendMessageToBackend:)``

フロントエンドからバックエンドへのメッセージ送信を委譲する。

## Objective-C Declaration
```objective-c
- (void)inspectorViewController:(_WKRemoteWebInspectorViewController *)controller sendMessageToBackend:(NSString *)message;
```

## Discussion
`_WKRemoteWebInspectorViewController` が `sendMessageToBackend:` の呼び出し時に、`respondsToSelector:` を確認してデリゲートへ転送する。

## References
- [`_WKRemoteWebInspectorViewController.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L58)
- [`_WKRemoteWebInspectorViewController.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L149)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
