# ``WKInternalsNotes/WKWebView/_dumpPrivateClickMeasurement(_:)``

`_dumpPrivateClickMeasurement` を実行する。

## Objective-C Declaration
```objective-c
- (void)_dumpPrivateClickMeasurement:(void(^)(NSString *))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`API/Cocoa/WKWebViewPrivateForTesting.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivateForTesting.h#L134)
- [`API/Cocoa/WKWebViewTesting.mm#L606`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewTesting.mm#L606)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
