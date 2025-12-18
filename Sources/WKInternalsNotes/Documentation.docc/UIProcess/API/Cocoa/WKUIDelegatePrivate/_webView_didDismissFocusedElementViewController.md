# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didDismissFocusedElementViewController:)``

フォーカス要素のフルスクリーン入力 UI の dismiss を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didDismissFocusedElementViewController:(UIViewController *)controller WK_API_AVAILABLE(ios(12.0));
```

## Discussion
フルスクリーン入力ビューの dismiss 後に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L296`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L296)
- [`WKContentViewInteraction.mm#L9073`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9073)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
