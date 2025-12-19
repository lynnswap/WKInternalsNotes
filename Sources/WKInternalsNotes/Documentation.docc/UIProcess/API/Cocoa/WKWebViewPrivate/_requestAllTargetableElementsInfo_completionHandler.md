# ``WKInternalsNotes/WKWebView/_requestAllTargetableElementsInfo(_:completionHandler:)``

`_requestAllTargetableElementsInfo` を取得する。

## Objective-C Declaration
```objective-c
- (void)_requestAllTargetableElementsInfo:(CGFloat)hitTestInterval completionHandler:(void(^)(NSArray<NSArray<_WKTargetedElementInfo *> *> *))completionHandler WK_API_AVAILABLE(visionos(2.0)) WK_API_UNAVAILABLE(macos, ios);
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L615`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L615)
- [`API/Cocoa/WKWebView.mm#L4573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L4573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
