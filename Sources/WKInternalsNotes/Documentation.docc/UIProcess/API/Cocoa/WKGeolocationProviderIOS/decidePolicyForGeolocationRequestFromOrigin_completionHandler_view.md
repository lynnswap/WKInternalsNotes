# ``WKInternalsNotes/WKGeolocationProviderIOS/decidePolicyForGeolocationRequestFromOrigin(_:completionHandler:view:)``

Geolocation 利用可否の判断フローを開始する。

## Objective-C Declaration
```objective-c
- (void)decidePolicyForGeolocationRequestFromOrigin:(WebKit::FrameInfoData&&)frameInfo completionHandler:(Function<void(bool)>&&)completionHandler view:(WKWebView*)view;
```

## Discussion
`frameInfo` と `view` の URL からリクエスト情報を作成してキューに積み、CoreLocation の認可確認を開始する。`_coreLocationProvider` がある場合は `requestGeolocationAuthorization` を呼び、無い場合は `CoreLocationGeolocationProvider::requestAuthorization` を呼んで `geolocationAuthorizationGranted` / `Denied` に委譲する。

## References
- [`WKGeolocationProviderIOS.h#L46`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.h#L46)
- [`WKGeolocationProviderIOS.mm#L159`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L159)
- [`WKGeolocationProviderIOS.mm#L169`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L169)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
