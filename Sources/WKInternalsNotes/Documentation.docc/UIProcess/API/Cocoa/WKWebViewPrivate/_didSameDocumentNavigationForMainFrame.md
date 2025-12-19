# ``WKInternalsNotes/WKWebView/_didSameDocumentNavigationForMainFrame(_:)``

`_didSameDocumentNavigationForMainFrame` を実行する。

## Objective-C Declaration
```objective-c
- (void)_didSameDocumentNavigationForMainFrame:(WebKit::SameDocumentNavigationType)navigationType;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L111`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L111)
- [`WKWebViewIOS.mm#L3407`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L3407)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
