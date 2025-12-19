# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/sendMessageToBackend(_:)``

リモートインスペクタのバックエンドへメッセージを転送する。

## Objective-C Declaration
```objective-c
- (void)sendMessageToBackend:(NSString *)message;
```

## Discussion
- RemoteWebInspectorUIProxyClient 経由で呼ばれ、delegate が `inspectorViewController:sendMessageToBackend:` を実装している場合に転送する。
- delegate が未設定 / 未実装の場合は no-op。

## References
- [`_WKRemoteWebInspectorViewController.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L58)
- [`_WKRemoteWebInspectorViewController.mm#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L70)
- [`_WKRemoteWebInspectorViewController.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L149)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
