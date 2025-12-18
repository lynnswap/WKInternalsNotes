# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:alternateURLFromImage:userInfo:)``

画像プレビュー用の代替 URL と userInfo を取得する。

## Objective-C Declaration
```objective-c
- (NSURL *)_webView:(WKWebView *)webView alternateURLFromImage:(UIImage *)image userInfo:(NSDictionary **)userInfo WK_API_AVAILABLE(ios(11.0));
```

## Discussion
WKContentViewInteraction の画像コンテキストメニュー処理で呼ばれ、返された URL と userInfo をプレビューに使用する。

## References
- [`WKUIDelegatePrivate.h#L272`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L272)
- [`WKContentViewInteraction.mm#L14942`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14942)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
