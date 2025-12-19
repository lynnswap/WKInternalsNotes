# ``WKInternalsNotes/WKWebView/_setPrivateClickMeasurementAttributionTokenPublicKeyURLForTesting(_:completionHandler:)``

`_setPrivateClickMeasurementAttributionTokenPublicKeyURLForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateClickMeasurementAttributionTokenPublicKeyURLForTesting:(NSURL *)url completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L131)
- [`API/Cocoa/WKWebViewTesting.mm#L573`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L573)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
