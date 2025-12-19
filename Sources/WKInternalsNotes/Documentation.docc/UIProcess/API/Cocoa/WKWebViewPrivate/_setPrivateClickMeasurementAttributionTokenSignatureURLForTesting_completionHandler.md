# ``WKInternalsNotes/WKWebView/_setPrivateClickMeasurementAttributionTokenSignatureURLForTesting(_:completionHandler:)``

`_setPrivateClickMeasurementAttributionTokenSignatureURLForTesting` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setPrivateClickMeasurementAttributionTokenSignatureURLForTesting:(NSURL *)url completionHandler:(void(^)(void))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
`completionHandler` に結果を返す。

## References
- [`WKWebViewPrivateForTesting.h#L132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L132)
- [`WKWebViewTesting.mm#L584`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L584)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
