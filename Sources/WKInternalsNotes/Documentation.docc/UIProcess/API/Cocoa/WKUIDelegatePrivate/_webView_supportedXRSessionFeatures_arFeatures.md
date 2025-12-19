# ``WKInternalsNotes/WKUIDelegatePrivate/_webView(_:supportedXRSessionFeatures:arFeatures:)``

XR セッションの対応 feature を delegate から取得する。

## Objective-C Declaration
```objective-c
- (void)_webView:(WKWebView *)webView supportedXRSessionFeatures:(_WKXRSessionFeatureFlags *)vrFeatures arFeatures:(_WKXRSessionFeatureFlags *)arFeatures WK_API_AVAILABLE(ios(18.0), visionos(2.0));
```

## Discussion
delegate が VR/AR 用 feature flags を設定し、UIClient が `PlatformXR` 用の feature list に変換して保持する。

## References
- [`WKUIDelegatePrivate.h#L185`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKUIDelegatePrivate.h#L185)
- [`UIDelegate.mm#L213`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Cocoa/UIDelegate.mm#L213)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
