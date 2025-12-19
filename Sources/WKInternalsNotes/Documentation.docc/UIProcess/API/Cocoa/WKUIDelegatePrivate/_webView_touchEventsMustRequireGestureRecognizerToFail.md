# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:touchEventsMustRequireGestureRecognizerToFail:)``

タッチイベントがジェスチャの失敗待ちを要求すべきか delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webView:(WKWebView *)webView touchEventsMustRequireGestureRecognizerToFail:(UIGestureRecognizer *)gestureRecognizer WK_API_AVAILABLE(ios(15.0));
```

## Discussion
WKContentViewInteraction がナビゲーションスワイプでは常に `YES` を返し、それ以外は delegate に委ねる。

## References
- [`WKUIDelegatePrivate.h#L277`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L277)
- [`WKContentViewInteraction.mm#L2191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2191)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
