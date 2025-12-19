# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:didPresentFocusedElementViewController:)``

フォーカス要素のフルスクリーン入力 UI の表示を通知する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView didPresentFocusedElementViewController:(UIViewController *)controller WK_API_AVAILABLE(ios(12.0));
```

## Discussion
表示トランジション完了後に delegate を呼び出す。

## References
- [`WKUIDelegatePrivate.h#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L272)
- [`WKContentViewInteraction.mm#L9045`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L9045)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
