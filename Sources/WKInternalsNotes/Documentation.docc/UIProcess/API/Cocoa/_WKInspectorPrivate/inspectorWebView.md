# ``WKInternalsNotes/_WKInspector/inspectorWebView()``

インスペクタフロントエンドの WKWebView を返す。

## Objective-C Declaration
```objective-c
- (WKWebView *)inspectorWebView;
```

## Default Value
`nil`（フロントエンド未作成時）

## Discussion
`WebInspectorUIProxy::inspectorPage()` の `cocoaView` を返すため、`connect` / `show` でフロントエンドが作られた後に利用可能になる。`inspectorPage` が `nil` の場合は `nil` を返す。

## References
- [`_WKInspectorPrivateForTesting.h#L31`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorPrivateForTesting.h#L31)
- [`_WKInspectorTesting.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L48)
- [`WebInspectorUIProxy.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
