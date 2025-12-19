# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:getAlternateURLFromImage:completionHandler:)``

画像の代替 URL と userInfo を非同期に delegate から取得する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView getAlternateURLFromImage:(UIImage *)image completionHandler:(void (^)(NSURL *alternateURL, NSDictionary *userInfo))completionHandler WK_API_AVAILABLE(ios(11.0));
```

## Discussion
ActionSheetAssistant の `getAlternateURLForImage` で delegate が実装されていれば呼び出し、返却値を completion に転送する。未実装の場合は `nil` を返す。

## References
- [`WKUIDelegatePrivate.h#L250`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L250)
- [`WKContentViewInteraction.mm#L10158`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10158)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
