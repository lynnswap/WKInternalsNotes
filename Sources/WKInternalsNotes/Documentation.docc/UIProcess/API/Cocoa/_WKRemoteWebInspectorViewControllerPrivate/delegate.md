# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/delegate``

リモートインスペクタのバックエンド通信とクローズ通知の受け取り先を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <_WKRemoteWebInspectorViewControllerDelegate> delegate;
```

## Default Value
`nil`

## Discussion
RemoteWebInspectorUIProxy から `sendMessageToBackend:` / `closeFromFrontend` が呼ばれた際、delegate が対応するセレクタを実装していれば通知する。

## References
- [`_WKRemoteWebInspectorViewController.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L43)
- [`_WKRemoteWebInspectorViewController.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L56)
- [`_WKRemoteWebInspectorViewController.mm#L149`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L149)
- [`_WKRemoteWebInspectorViewController.mm#L156`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L156)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
