# ``WKInternalsNotes/WKWebView/_beginAnimatedResizeWithUpdates(_:)``

`_beginAnimatedResizeWithUpdates` を開始する。

## Objective-C Declaration
```objective-c
- (void)_beginAnimatedResizeWithUpdates:(void (^)(void))updateBlock;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L751`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L751)
- [`WKWebViewIOS.mm#L4579`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4579)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
