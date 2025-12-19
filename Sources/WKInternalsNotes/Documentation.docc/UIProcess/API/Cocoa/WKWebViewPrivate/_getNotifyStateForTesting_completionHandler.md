# ``WKInternalsNotes/WKWebView/_getNotifyStateForTesting(_:completionHandler:)``

`_getNotifyStateForTesting` を取得する。

## Objective-C Declaration
```objective-c
- (void)_getNotifyStateForTesting:(NSString *)notificationName completionHandler:(void(^)(NSNumber * _Nullable))completionHandler WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L155`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L155)
- [`API/Cocoa/WKWebViewTesting.mm#L945`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L945)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
