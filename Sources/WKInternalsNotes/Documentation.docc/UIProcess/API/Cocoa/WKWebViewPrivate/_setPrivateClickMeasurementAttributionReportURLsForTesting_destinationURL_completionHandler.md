# ``WKInternalsNotes/WKWebView/_setPrivateClickMeasurementAttributionReportURLsForTesting(_:destinationURL:completionHandler:)``

`_setPrivateClickMeasurementAttributionReportURLsForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateClickMeasurementAttributionReportURLsForTesting:(NSURL *)sourceURL destinationURL:(NSURL *)destinationURL completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTesting.h#L130`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L130)
- [`WKWebViewTesting.mm#L562`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L562)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
