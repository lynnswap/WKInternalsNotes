# ``WKInternalsNotes/WKWebView/_showingNavigationGestureSnapshot``

`_showingNavigationGestureSnapshot` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isShowingNavigationGestureSnapshot) BOOL _showingNavigationGestureSnapshot;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isShowingNavigationGestureSnapshot`。

## References
- [`WKWebViewPrivate.h#L270`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L270)
- [`WKWebView.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
