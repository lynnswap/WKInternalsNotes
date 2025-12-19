# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/sendMessageToFrontend(_:)``

リモートインスペクタのフロントエンドへメッセージを送信する。

## Objective-C Declaration
```objective-c
- (void)sendMessageToFrontend:(NSString *)message;
```

## Discussion
RemoteWebInspectorUIProxy に委譲し、inspector page が存在する場合に IPC を送る。フロントエンド未作成時は送信されない。

## References
- [`_WKRemoteWebInspectorViewController.h#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L52)
- [`_WKRemoteWebInspectorViewController.mm#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L142)
- [`RemoteWebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
