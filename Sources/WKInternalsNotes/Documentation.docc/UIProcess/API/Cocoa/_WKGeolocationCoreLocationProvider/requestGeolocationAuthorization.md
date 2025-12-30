# ``WKInternalsNotes/_WKGeolocationCoreLocationProvider/requestGeolocationAuthorization()``

アプリのジオロケーション許可を要求する。

## Objective-C Declaration
```objective-c
- (void)requestGeolocationAuthorization;
```

## Discussion
`WKGeolocationProviderIOS` が geolocation 要求時に `_coreLocationProvider requestGeolocationAuthorization` を呼ぶ。

## References
- [`_WKGeolocationCoreLocationProvider.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L48)
- [`WKGeolocationProviderIOS.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L159)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
