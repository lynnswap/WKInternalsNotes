# ``WKInternalsNotes/WKWebView/_getRenderTreeAsStringWithCompletionHandler(_:)``

`_getRenderTreeAsStringWithCompletionHandler` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getRenderTreeAsStringWithCompletionHandler:(NS_SWIFT_UI_ACTOR void (^)(NSString * NS_NULLABLE_RESULT, NSError * _Nullable error))completionHandler WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivateForTesting.h#L100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L100)
- [`WKWebViewTesting.mm#L658`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L658)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
