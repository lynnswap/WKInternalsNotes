# ``WKInternalsNotes/_WKGeolocationCoreLocationProvider/setListener(_:)``

Core Location 更新を受け取る listener を設定する。

## Objective-C Declaration
```objective-c
- (void)setListener:(id <_WKGeolocationCoreLocationListener>)listener;
```

## Discussion
`WKGeolocationProviderIOS` が `_coreLocationProvider` を持つ場合に `self` を listener として設定する。

## References
- [`_WKGeolocationCoreLocationProvider.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L47)
- [`WKGeolocationProviderIOS.mm#L154`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L154)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
