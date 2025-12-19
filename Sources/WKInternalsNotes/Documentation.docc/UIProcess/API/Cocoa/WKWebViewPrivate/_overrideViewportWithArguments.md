# ``WKInternalsNotes/WKWebView/_overrideViewportWithArguments(_:)``

`_overrideViewportWithArguments` を実行する。

## Objective-C Declaration
```objective-c
- (void)_overrideViewportWithArguments:(NSDictionary<NSString *, NSString *> *)arguments WK_API_AVAILABLE(ios(13.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L761`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L761)
- [`WKWebViewIOS.mm#L4944`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4944)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
