# ``WKInternalsNotes/WKWebView/currentlyVisibleContentInsetsWithScale(_:obscuredInsets:)``

`currentlyVisibleContentInsetsWithScale` を実行する。

## Objective-C Declaration
```objective-c
- (UIEdgeInsets)currentlyVisibleContentInsetsWithScale:(CGFloat)scaleFactor obscuredInsets:(UIEdgeInsets)obscuredInsets;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L241)
- [`WKWebViewIOS.mm#L3096`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3096)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
