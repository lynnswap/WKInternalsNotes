# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:startXRSessionWithCompletionHandler:)``

XR セッション開始を delegate に依頼する（旧シグネチャ）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView startXRSessionWithCompletionHandler:(void (^)(id))completionHandler WK_API_AVAILABLE(macos(12.0), ios(15.0));
```

## Discussion
UIClient が新 API 未実装時に使用し、結果のみを返して `UIViewController` は `nil` で補完する。

## References
- [`WKUIDelegatePrivate.h#L210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L210)
- [`UIDelegate.mm#L2248`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2248)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
