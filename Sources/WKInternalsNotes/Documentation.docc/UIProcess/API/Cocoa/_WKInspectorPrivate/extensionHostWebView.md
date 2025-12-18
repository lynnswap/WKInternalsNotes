# ``WKInternalsNotes/_WKInspector/extensionHostWebView``

インスペクタ拡張タブのホストとして使われるフロントエンド WKWebView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKWebView *extensionHostWebView;
```

## Default Value
`nil`（インスペクタのフロントエンド未作成時）

## Discussion
実装は `self.inspectorWebView` を返すだけで、`inspectorWebView` は `WebInspectorUIProxy::inspectorPage()` の `cocoaView` から生成される。フロントエンドが未作成の場合は `nil` になる。

## References
- [`_WKInspectorPrivate.h#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorPrivate.h#L35)
- [`_WKInspector.mm#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L237)
- [`_WKInspectorTesting.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorTesting.mm#L48)
- [`WebInspectorUIProxy.h#L125`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L125)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
