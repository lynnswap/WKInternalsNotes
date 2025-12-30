# ``WKInternalsNotes/_WKGeolocationCoreLocationProvider/stop()``

WebCore が更新停止した際に位置更新を停止する。

## Objective-C Declaration
```objective-c
- (void)stop;
```

## Discussion
`WKGeolocationProviderIOS` の `_stopUpdating` が `_coreLocationProvider stop` を呼び出す。

## References
- [`_WKGeolocationCoreLocationProvider.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L50)
- [`WKGeolocationProviderIOS.mm#L113`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L113)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
