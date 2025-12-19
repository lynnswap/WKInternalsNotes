# ``WKInternalsNotes/WKWebView/_prepareForMoveToWindow(_:completionHandler:)``

`_prepareForMoveToWindow` を実行する。

## Objective-C Declaration
```objective-c
- (void)_prepareForMoveToWindow:(NSWindow *)targetWindow completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(10.13));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L914`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L914)
- [`WKWebViewMac.mm#L2030`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L2030)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
