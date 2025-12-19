# ``WKInternalsNotes/WKWebView/_mediaCaptureReportingDelayForTesting``

`_mediaCaptureReportingDelayForTesting` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMediaCaptureReportingDelayForTesting:) double _mediaCaptureReportingDelayForTesting WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMediaCaptureReportingDelayForTesting:`。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L77)
- [`API/Cocoa/WKWebViewTesting.mm#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L462)
- [`API/Cocoa/WKWebViewTesting.mm#L467`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L467)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
