# ``WKInternalsNotes/WKWebView/_scrollbarStateForScrollingNodeID(_:processID:isVertical:)``

`_scrollbarStateForScrollingNodeID` を実行する。

## Objective-C Declaration
```objective-c
- (NSString*)_scrollbarStateForScrollingNodeID:(uint64_t)scrollingNodeID processID:(uint64_t)processID isVertical:(bool)isVertical;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L58)
- [`API/Cocoa/WKWebViewTesting.mm#L503`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L503)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
