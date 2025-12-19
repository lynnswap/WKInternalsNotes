# ``WKInternalsNotes/WKWebView/_animatingDragCancel``

`_animatingDragCancel` の値を取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isAnimatingDragCancel) BOOL _animatingDragCancel;
```

## Discussion
読み取り専用のため setter は持たない。 getter は `_isAnimatingDragCancel`。

## References
- [`API/ios/WKWebViewPrivateForTestingIOS.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewPrivateForTestingIOS.h#L49)
- [`API/ios/WKWebViewTestingIOS.mm#L384`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewTestingIOS.mm#L384)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
