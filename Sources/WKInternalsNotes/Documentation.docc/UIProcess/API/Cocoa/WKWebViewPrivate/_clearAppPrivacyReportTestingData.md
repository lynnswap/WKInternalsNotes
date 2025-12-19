# ``WKInternalsNotes/WKWebView/_clearAppPrivacyReportTestingData(_:)``

`_clearAppPrivacyReportTestingData` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_clearAppPrivacyReportTestingData:(void(^)(void))completionHandler;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L138`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L138)
- [`API/Cocoa/WKWebViewTesting.mm#L679`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L679)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
