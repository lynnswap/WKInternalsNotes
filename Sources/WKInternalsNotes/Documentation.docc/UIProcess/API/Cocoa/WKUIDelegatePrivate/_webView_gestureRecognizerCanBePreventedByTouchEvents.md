# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:gestureRecognizerCanBePreventedByTouchEvents:)``

タッチイベントによりジェスチャが阻止可能かを delegate に確認する。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView gestureRecognizerCanBePreventedByTouchEvents:(UIGestureRecognizer *)gestureRecognizer WK_API_AVAILABLE(ios(16.5));
```

## Discussion
WKContentViewInteraction が `_gestureRecognizerCanBePreventedByTouchEvents:` から delegate に問い合わせ、ジェスチャの制御可否を決定する。

## References
- [`WKUIDelegatePrivate.h#L302`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L302)
- [`WKContentViewInteraction.mm#L2198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2198)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
