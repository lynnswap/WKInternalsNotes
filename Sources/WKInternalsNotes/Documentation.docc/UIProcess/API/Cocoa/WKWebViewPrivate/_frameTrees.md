# ``WKInternalsNotes/WKWebView/_frameTrees(_:)``

`_frameTrees` を実行する。

## Objective-C Declaration
```objective-c
- (void)_frameTrees:(void (^)(NSSet<_WKFrameTreeNode *> *))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L241`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L241)
- [`API/Cocoa/WKWebView.mm#L3855`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3855)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
