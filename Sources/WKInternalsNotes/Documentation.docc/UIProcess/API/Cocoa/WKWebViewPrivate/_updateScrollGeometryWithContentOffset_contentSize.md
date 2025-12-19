# ``WKInternalsNotes/WKWebView/_updateScrollGeometryWithContentOffset(_:contentSize:)``

`_updateScrollGeometryWithContentOffset` を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateScrollGeometryWithContentOffset:(CGPoint)contentOffset contentSize:(CGSize)contentSize;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewInternal.h#L604`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewInternal.h#L604)
- [`API/Cocoa/WKWebView.mm#L3041`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L3041)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
