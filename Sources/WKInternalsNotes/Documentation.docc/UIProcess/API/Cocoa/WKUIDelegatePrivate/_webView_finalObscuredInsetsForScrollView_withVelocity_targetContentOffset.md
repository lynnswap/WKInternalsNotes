# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:finalObscuredInsetsForScrollView:withVelocity:targetContentOffset:)``

スクロール終了時の最終的な隠し領域インセットを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (UIEdgeInsets)_webView:(WKWebView *)webView finalObscuredInsetsForScrollView:(UIScrollView *)scrollView withVelocity:(CGPoint)velocity targetContentOffset:(inout CGPoint *)targetContentOffset WK_API_AVAILABLE(ios(9.0));
```

## Discussion
非同期スクロール時に delegate へ問い合わせ、返答がない場合は `_computedObscuredInset` を使う。取得したインセットを `UIEdgeInsetsInsetRect` に反映し、スナップ位置調整に利用する。

## References
- [`WKUIDelegatePrivate.h#L265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L265)
- [`WKWebViewIOS.mm#L2334`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L2334)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
