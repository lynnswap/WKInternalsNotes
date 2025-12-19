# ``WKInternalsNotes/_WKInspector/webView``

検査対象の WKWebView を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WKWebView *webView;
```

## Default Value
検査対象ページが存在する場合はその `WKWebView`。`_inspector->inspectedPage()` が `nil` の場合は `nil`。

## Discussion
`WebInspectorUIProxy::inspectedPage()` から取得した `WebPageProxy` の `cocoaView` を返す。検査対象ページが破棄された場合は `nil` になる。

## References
- [`_WKInspector.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L45)
- [`_WKInspector.mm#L109`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L109)
- [`WebInspectorUIProxy.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
