# ``WKInternalsNotes/_WKGeolocationCoreLocationProvider/setEnableHighAccuracy(_:)``

高精度測位の有効/無効を切り替える。

## Objective-C Declaration
```objective-c
- (void)setEnableHighAccuracy:(BOOL)flag;
```

## Discussion
`WKGeolocationProviderIOS` の `_setEnableHighAccuracy` が `_coreLocationProvider setEnableHighAccuracy:` を呼ぶ。

## References
- [`_WKGeolocationCoreLocationProvider.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L51)
- [`WKGeolocationProviderIOS.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L120)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
