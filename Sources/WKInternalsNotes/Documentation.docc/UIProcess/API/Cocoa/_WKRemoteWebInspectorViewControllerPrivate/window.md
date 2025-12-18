# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/window``

リモートインスペクタ UI の NSWindow を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly, retain) NSWindow *window;
```

## Default Value
`nil`（フロントエンド生成前）

## Discussion
`RemoteWebInspectorUIProxy::window()` を返す。`initialize` によってフロントエンドページとウインドウが作成され、以降 `window` が利用可能になる。

## References
- [`_WKRemoteWebInspectorViewController.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L45)
- [`_WKRemoteWebInspectorViewController.mm#L117`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L117)
- [`RemoteWebInspectorUIProxy.h#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.h#L113)
- [`RemoteWebInspectorUIProxy.cpp#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.cpp#L88)
- [`RemoteWebInspectorUIProxyMac.mm#L116`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/RemoteWebInspectorUIProxyMac.mm#L116)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
