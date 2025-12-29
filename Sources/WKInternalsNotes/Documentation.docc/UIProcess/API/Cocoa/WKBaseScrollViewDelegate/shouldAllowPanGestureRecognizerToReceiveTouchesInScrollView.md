# ``WKInternalsNotes/WKBaseScrollViewDelegate/shouldAllowPanGestureRecognizerToReceiveTouchesInScrollView(_:)``

パンジェスチャがタッチを受け取ってよいかを判断する。

## Objective-C Declaration
```objective-c
- (BOOL)shouldAllowPanGestureRecognizerToReceiveTouchesInScrollView:(WKBaseScrollView *)scrollView;
```

## Discussion
`WKWebView` 実装では互換ポインタタッチのシミュレーション中は `NO` を返し、それ以外は `YES`。

## References
- [`WKWebViewIOS.mm#L4146`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4146)
- [`WKBaseScrollView.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
