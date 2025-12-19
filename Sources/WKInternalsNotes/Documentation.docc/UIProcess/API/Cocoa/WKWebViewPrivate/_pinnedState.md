# ``WKInternalsNotes/WKWebView/_pinnedState``

`_pinnedState` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKRectEdge _pinnedState WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
読み取り専用のため setter は持たない。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L836`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L836)
- [`API/mac/WKWebViewMac.mm#L1492`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1492)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
