# ``WKInternalsNotes/WKNavigationAction/_storeSKAdNetworkAttribution()``

SKAdNetwork のアトリビューション情報を保存する。

## Objective-C Declaration
```objective-c
- (void)_storeSKAdNetworkAttribution WK_API_AVAILABLE(macos(13.0), ios(16.1));
```

## Discussion
mainFrameNavigation の private click measurement が SKAdNetwork 用である場合に、source frame からページを取得して `WebsiteDataStore::storePrivateClickMeasurement` を呼ぶ。いずれかの参照が無い場合は何もしない。

## References
- [`WKNavigationActionPrivate.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L64)
- [`WKNavigationAction.mm#L243`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L243)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
