# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/loadForDebuggable(_:backendCommandsURL:)``

指定 debuggable 情報と backendCommandsURL を使ってリモートインスペクタを起動する。

## Objective-C Declaration
```objective-c
- (void)loadForDebuggable:(_WKInspectorDebuggableInfo *)debuggableInfo backendCommandsURL:(NSURL *)backendCommandsURL WK_API_AVAILABLE(macos(12.0));
```

## Discussion
RemoteWebInspectorUIProxy の `initialize` を呼び、debuggable 情報と URL を保存してフロントエンドページ/ウインドウを作成し、Initialize メッセージと inspector page URL を送る。

## References
- [`_WKRemoteWebInspectorViewController.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L50)
- [`_WKRemoteWebInspectorViewController.mm#L127`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L127)
- [`RemoteWebInspectorUIProxy.cpp#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.cpp#L88)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
