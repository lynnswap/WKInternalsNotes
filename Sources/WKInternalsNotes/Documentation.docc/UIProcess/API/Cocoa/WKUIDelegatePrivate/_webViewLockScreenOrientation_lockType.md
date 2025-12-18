# ``WKInternalsNotes/WKUIDelegatePrivate/_webViewLockScreenOrientation(_:lockType:)``

画面回転のロック要求を delegate に問い合わせる。

## Objective-C Declaration
```objective-c
- (BOOL)_webViewLockScreenOrientation:(WKWebView *)webView lockType:(_WKScreenOrientationType)lockType WK_API_AVAILABLE(ios(16.4));
```

## Discussion
UIDelegate::UIClient が `lockType` を `_WKScreenOrientationType` に変換して delegate に渡し、結果を返す。

## References
- [`WKUIDelegatePrivate.h#L291`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L291)
- [`UIDelegate.mm#L743`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L743)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
