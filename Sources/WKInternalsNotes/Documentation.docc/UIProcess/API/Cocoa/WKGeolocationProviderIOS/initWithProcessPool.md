# ``WKInternalsNotes/WKGeolocationProviderIOS/initWithProcessPool(_:)``

ProcessPool に紐づく geolocation provider を初期化する。

## Objective-C Declaration
```objective-c
- (id)initWithProcessPool:(WebKit::WebProcessPool&)processPool;
```

## Discussion
`processPool` に `_coreLocationProvider` が設定されている場合、`WebGeolocationManagerProxy` に provider callback を登録し、`_coreLocationProvider` を保持して listener を設定する。未設定の場合は provider を登録しない。

## References
- [`WKGeolocationProviderIOS.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.h#L45)
- [`WKGeolocationProviderIOS.mm#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L134)
- [`WKGeolocationProviderIOS.mm#L152`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L152)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
