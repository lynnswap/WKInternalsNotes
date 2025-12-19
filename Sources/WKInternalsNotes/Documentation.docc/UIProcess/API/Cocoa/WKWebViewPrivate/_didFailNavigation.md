# ``WKInternalsNotes/WKWebView/_didFailNavigation(_:)``

`_didFailNavigation` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didFailNavigation:(API::Navigation*)navigation;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/ios/WKWebViewIOS.h#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L110)
- [`API/ios/WKWebViewIOS.mm#L3401`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3401)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
