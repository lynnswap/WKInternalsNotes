# ``WKInternalsNotes/WKWebView/_clearServiceWorkerEntitlementOverride(_:)``

`_clearServiceWorkerEntitlementOverride` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_clearServiceWorkerEntitlementOverride:(void (^)(void))completionHandler WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L462`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L462)
- [`WKWebView.mm#L5749`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L5749)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
