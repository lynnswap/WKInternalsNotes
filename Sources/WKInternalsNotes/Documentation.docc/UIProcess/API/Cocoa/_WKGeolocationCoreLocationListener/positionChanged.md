# ``WKInternalsNotes/_WKGeolocationCoreLocationListener/positionChanged(_:)``

位置更新を通知する。

## Objective-C Declaration
```objective-c
- (void)positionChanged:(_WKGeolocationPosition *)position;
```

## Discussion
`WKGeolocationProviderIOS` では `position` を `_lastActivePosition` に保存し、`_geolocationManager->providerDidChangePosition` を呼ぶ。

## References
- [`_WKGeolocationCoreLocationProvider.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L40)
- [`WKGeolocationProviderIOS.mm#L219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L219)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
