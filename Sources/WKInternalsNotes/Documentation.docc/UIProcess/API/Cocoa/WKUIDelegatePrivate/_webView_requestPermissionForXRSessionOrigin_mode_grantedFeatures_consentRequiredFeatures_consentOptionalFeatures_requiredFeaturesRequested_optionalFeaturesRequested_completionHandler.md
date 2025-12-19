# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:requestPermissionForXRSessionOrigin:mode:grantedFeatures:consentRequiredFeatures:consentOptionalFeatures:requiredFeaturesRequested:optionalFeaturesRequested:completionHandler:)``

XR セッションの権限を delegate に問い合わせる（requested features 付き）。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView requestPermissionForXRSessionOrigin:(NSString *)originString mode:(_WKXRSessionMode)mode grantedFeatures:(_WKXRSessionFeatureFlags)grantedFeatures consentRequiredFeatures:(_WKXRSessionFeatureFlags)consentRequiredFeatures consentOptionalFeatures:(_WKXRSessionFeatureFlags)consentOptionalFeatures requiredFeaturesRequested:(_WKXRSessionFeatureFlags)requiredFeaturesRequested optionalFeaturesRequested:(_WKXRSessionFeatureFlags)optionalFeaturesRequested completionHandler:(void (^)(_WKXRSessionFeatureFlags))completionHandler WK_API_AVAILABLE(macos(14.0), ios(17.0));
```

## Discussion
UIDelegate::UIClient が requested features を含めて delegate に渡し、`CompletionHandlerCallChecker` で応答を処理する。

## References
- [`WKUIDelegatePrivate.h#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L185)
- [`UIDelegate.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
