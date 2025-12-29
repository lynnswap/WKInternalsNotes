# ``WKInternalsNotes/_WKGeolocationCoreLocationListener/errorOccurred(_:)``

位置情報取得エラーを通知する。

## Objective-C Declaration
```objective-c
- (void)errorOccurred:(NSString *)errorMessage;
```

## Discussion
`_geolocationManager->providerDidFailToDeterminePosition(errorMessage)` を呼び出す。

## References
- [`_WKGeolocationCoreLocationProvider.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L41)
- [`WKGeolocationProviderIOS.mm#L225`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L225)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
