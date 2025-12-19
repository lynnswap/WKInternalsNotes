# ``WKInternalsNotes/WKWebView/_appPrivacyReportTestingData(_:)``

`_appPrivacyReportTestingData` を実行する。

## Objective-C Declaration
```objective-c
- (void)_appPrivacyReportTestingData:(void(^)(struct WKAppPrivacyReportTestingData data))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L137)
- [`API/Cocoa/WKWebViewTesting.mm#L672`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L672)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
