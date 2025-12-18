# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestPermissionForXRSessionOrigin:mode:grantedFeatures:consentRequiredFeatures:consentOptionalFeatures:completionHandler:)``

XR セッションの権限を delegate に問い合わせる（旧シグネチャ）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestPermissionForXRSessionOrigin:(NSString *)originString mode:(_WKXRSessionMode)mode grantedFeatures:(_WKXRSessionFeatureFlags)grantedFeatures consentRequiredFeatures:(_WKXRSessionFeatureFlags)consentRequiredFeatures consentOptionalFeatures:(_WKXRSessionFeatureFlags)consentOptionalFeatures completionHandler:(void (^)(_WKXRSessionFeatureFlags))completionHandler WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Discussion
UIDelegate::UIClient が新シグネチャ未実装時にこの旧 API を使い、`_WKXRSessionFeatureFlags` を渡して許可された features を受け取る。

## References
- [`WKUIDelegatePrivate.h#L207`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L207)
- [`UIDelegate.mm#L2169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L2169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
