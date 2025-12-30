# ``WKInternalsNotes/_WKTextManipulationDelegate/_webView(_:didFindTextManipulationItems:)``

テキスト操作対象のアイテム配列を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFindTextManipulationItems:(NSArray<_WKTextManipulationItem *> *)items;
```

## Discussion
`_startTextManipulationsWithConfiguration:` のコールバックで、`_WKTextManipulationItem` へ変換した配列を渡す。

## References
- [`_WKTextManipulationDelegate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationDelegate.h#L36)
- [`WKWebView.mm#L3991`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3991)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
