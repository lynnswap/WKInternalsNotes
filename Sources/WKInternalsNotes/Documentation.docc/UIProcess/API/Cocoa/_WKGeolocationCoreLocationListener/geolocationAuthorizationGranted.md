# ``WKInternalsNotes/_WKGeolocationCoreLocationListener/geolocationAuthorizationGranted()``

ジオロケーション許可が付与された後の処理を進める。

## Objective-C Declaration
```objective-c
- (void)geolocationAuthorizationGranted;
```

## Discussion
待機中のリクエストが空なら何もしない。先頭のリクエストを取り出し、UI delegate の `_webView:requestGeolocationAuthorizationForURL:frame:decisionHandler:` があればそれを呼ぶ。未実装の場合は `WKWebGeolocationPolicyDecider` にフォールバックし、結果を完了ハンドラに渡した後に次のリクエスト処理へ進む。

## References
- [`_WKGeolocationCoreLocationProvider.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKGeolocationCoreLocationProvider.h#L38)
- [`WKGeolocationProviderIOS.mm#L183`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKGeolocationProviderIOS.mm#L183)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
