# ``WKInternalsNotes/WKWebView/_setPrivateClickMeasurementAppBundleIDForTesting(_:completionHandler:)``

`_setPrivateClickMeasurementAppBundleIDForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateClickMeasurementAppBundleIDForTesting:(NSString *)appBundleID completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L133)
- [`API/Cocoa/WKWebViewTesting.mm#L595`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L595)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
