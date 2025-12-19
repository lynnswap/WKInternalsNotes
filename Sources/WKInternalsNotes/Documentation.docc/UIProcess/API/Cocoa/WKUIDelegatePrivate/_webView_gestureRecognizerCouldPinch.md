# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:gestureRecognizerCouldPinch:)``

ピンチジェスチャがズームにつながるかを delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView gestureRecognizerCouldPinch:(UIGestureRecognizer *)gestureRecognizer WK_API_AVAILABLE(ios(13.0));
```

## Discussion
スクロールビュー以外の `UIPinchGestureRecognizer` が対象のとき、delegate の返答でズーム可否を判断する。

## References
- [`WKUIDelegatePrivate.h#L274`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L274)
- [`WKContentViewInteraction.mm#L2371`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2371)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
