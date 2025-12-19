# ``WKInternalsNotes/WKWebView/_isForcedIntoAppBoundMode(_:)``

`_isForcedIntoAppBoundMode` の状態を返す。

## Objective-C Declaration
```objective-c
- (void)_isForcedIntoAppBoundMode:(void(^)(BOOL))completionHandler WK_API_AVAILABLE(ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L789`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L789)
- [`WKWebViewIOS.mm#L5060`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5060)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
