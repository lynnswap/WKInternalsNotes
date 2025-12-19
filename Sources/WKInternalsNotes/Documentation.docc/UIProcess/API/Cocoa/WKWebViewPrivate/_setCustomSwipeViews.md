# ``WKInternalsNotes/WKWebView/_setCustomSwipeViews(_:)``

`_setCustomSwipeViews` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setCustomSwipeViews:(NSArray *)customSwipeViews WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L892`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L892)
- [`WKWebViewMac.mm#L1946`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1946)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
