# ``WKInternalsNotes/_WKGeolocationCoreLocationListener/geolocationAuthorizationDenied()``

ジオロケーションの許可が拒否された場合の処理を行う。

## Objective-C Declaration
```objective-c
- (void)geolocationAuthorizationDenied;
```

## Discussion
待機中の全リクエストを取り出し、各 `completionHandler(false)` を呼び出す。

## References
- [`_WKGeolocationCoreLocationProvider.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L39)
- [`WKGeolocationProviderIOS.mm#L212`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L212)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
