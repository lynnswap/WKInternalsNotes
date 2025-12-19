# ``WKInternalsNotes/_WKRemoteWebInspectorViewController/webView``

リモートインスペクタのフロントエンド WKWebView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly, retain) WKWebView *webView;
```

## Default Value
`nil`（フロントエンド生成前）

## Discussion
`RemoteWebInspectorUIProxy::webView()` を返す。`initialize` によりフロントエンドが作成されると `WKInspectorViewController` の webView が構築され、ウインドウに追加される。

## References
- [`_WKRemoteWebInspectorViewController.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.h#L46)
- [`_WKRemoteWebInspectorViewController.mm#L122`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L122)
- [`RemoteWebInspectorUIProxy.h#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.h#L114)
- [`RemoteWebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/RemoteWebInspectorUIProxy.cpp)
- [`RemoteWebInspectorUIProxyMac.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/RemoteWebInspectorUIProxyMac.mm#L106)
- [`RemoteWebInspectorUIProxyMac.mm#L106`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/RemoteWebInspectorUIProxyMac.mm#L106)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
