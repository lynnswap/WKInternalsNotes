# ``WKInternalsNotes/WKWebView/_scrollToEdge(_:animated:)``

`_scrollToEdge` を実行する。

## Objective-C Declaration
```objective-c
- (void)_scrollToEdge:(_WKRectEdge)edge animated:(BOOL)animated;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewInternal.h#L682`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L682)
- [`WKWebView.mm#L6460`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6460)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
