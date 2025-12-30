# ``WKInternalsNotes/_WKGeolocationCoreLocationProvider/start()``

WebCore が更新開始した際に位置更新を開始する。

## Objective-C Declaration
```objective-c
- (void)start;
```

## Discussion
`WKGeolocationProviderIOS` の `_startUpdating` が `_coreLocationProvider start` を呼び出す。

## References
- [`_WKGeolocationCoreLocationProvider.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L49)
- [`WKGeolocationProviderIOS.mm#L102`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L102)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
