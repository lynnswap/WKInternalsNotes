# ``WKInternalsNotes/WKWebView/_accessibilityRetrieveRectsAtSelectionOffset(_:withText:completionHandler:)``

`_accessibilityRetrieveRectsAtSelectionOffset` を実行する。

## Objective-C Declaration
```objective-c
- (void)_accessibilityRetrieveRectsAtSelectionOffset:(NSInteger)offset withText:(NSString *)text completionHandler:(void (^)(NSArray<NSValue *> *rects))completionHandler WK_API_AVAILABLE(ios(11.3));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivate.h#L777`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L777)
- [`WKWebViewIOS.mm#L5007`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5007)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
