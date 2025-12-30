# ``WKInternalsNotes/_WKInspectorExtensionHost/extensionHostWebView``

拡張機能ホスト用の `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, readonly) WKWebView *extensionHostWebView;
```

## Default Value
`nil`（フロントエンド未作成時など）。

## Discussion
`_WKInspector` は `inspectorWebView`、`_WKRemoteWebInspectorViewController` は `webView` を返し、拡張のホストに使う `WKWebView` を公開する。

## References
- [`_WKInspectorExtensionHost.h#L80`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorExtensionHost.h#L80)
- [`_WKInspector.mm#L237`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L237)
- [`_WKRemoteWebInspectorViewController.mm#L173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKRemoteWebInspectorViewController.mm#L173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
