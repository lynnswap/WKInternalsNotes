# ``WKInternalsNotes/WKWebView/_frames(_:)``

`_frames` を実行する。

## Objective-C Declaration
```objective-c
- (void)_frames:(void (^)(_WKFrameTreeNode *))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L240`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L240)
- [`WKWebView.mm#L3846`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3846)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
