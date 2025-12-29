# ``WKInternalsNotes/WKBaseScrollViewDelegate/axesToPreventScrollingForPanGestureInScrollView(_:)``

パンジェスチャで抑止すべきスクロール軸を返す。

## Objective-C Declaration
```objective-c
- (UIAxis)axesToPreventScrollingForPanGestureInScrollView:(WKBaseScrollView *)scrollView;
```

## Discussion
`WKWebView` 実装では `WKContentView` の `preventsPanningInXAxis/YAxis` を参照して抑止軸を組み立てる。抑止がなければ `UIAxisNeither` を返し、必要に応じてポインタキャンセルを行う。

## References
- [`WKWebViewIOS.mm#L4151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4151)
- [`WKBaseScrollView.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKBaseScrollView.h#L49)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
