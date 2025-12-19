# ``WKInternalsNotes/WKWebView/_setPrivateClickMeasurementOverrideTimerForTesting(_:completionHandler:)``

`_setPrivateClickMeasurementOverrideTimerForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateClickMeasurementOverrideTimerForTesting:(BOOL)overrideTimer completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTesting.h#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L129)
- [`WKWebViewTesting.mm#L551`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L551)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
