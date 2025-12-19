# ``WKInternalsNotes/WKWebView/scrollView(_:handleScrollUpdate:completion:)``

`scrollView` を実行する。

## Objective-C Declaration
```objective-c
- (void)scrollView:(WKBaseScrollView *)scrollView handleScrollUpdate:(WKBEScrollViewScrollUpdate *)update completion:(void (^)(BOOL handled))completion;
```

## Discussion
`completion` に結果を返す。

## References
- [`API/ios/WKWebViewIOS.h#L192`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L192)
- [`API/Cocoa/WKWebView.mm#L1813`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L1813)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
