# ``WKInternalsNotes/_WKTextManipulationDelegate/_webView(_:didFindTextManipulationItem:)``

テキスト操作対象の単一アイテムを通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didFindTextManipulationItem:(_WKTextManipulationItem *)item;
```

## Discussion
`didFindTextManipulationItems:` が未実装の場合に、各アイテムごとに呼ばれる。

## References
- [`_WKTextManipulationDelegate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationDelegate.h#L36)
- [`WKWebView.mm#L3995`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3995)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
