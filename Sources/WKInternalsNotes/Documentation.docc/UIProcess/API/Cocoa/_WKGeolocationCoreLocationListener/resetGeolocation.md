# ``WKInternalsNotes/_WKGeolocationCoreLocationListener/resetGeolocation()``

ジオロケーション権限の状態をリセットする。

## Objective-C Declaration
```objective-c
- (void)resetGeolocation;
```

## Discussion
`_geolocationManager->resetPermissions()` を呼び出す。

## References
- [`_WKGeolocationCoreLocationProvider.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L42)
- [`WKGeolocationProviderIOS.mm#L230`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L230)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
