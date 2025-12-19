# ``WKInternalsNotes/WKWebView/_setStatisticsCrossSiteLoadWithLinkDecorationForTesting(_:withToHost:withWasFiltered:withCompletionHandler:)``

`_setStatisticsCrossSiteLoadWithLinkDecorationForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setStatisticsCrossSiteLoadWithLinkDecorationForTesting:(NSString *)fromHost withToHost:(NSString *)toHost withWasFiltered:(BOOL)wasFiltered withCompletionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(15.0), ios(18.0), visionos(2.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L609`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L609)
- [`API/Cocoa/WKWebView.mm#L4451`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4451)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
