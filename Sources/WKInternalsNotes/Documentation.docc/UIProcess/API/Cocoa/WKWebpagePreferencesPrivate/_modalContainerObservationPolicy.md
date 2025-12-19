# ``WKInternalsNotes/WKWebpagePreferences/_modalContainerObservationPolicy``

モーダルコンテナの観測ポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setModalContainerObservationPolicy:) _WKWebsiteModalContainerObservationPolicy _modalContainerObservationPolicy WK_API_AVAILABLE(macos(13.0), ios(16.0));
```

## Default Value
初期値は `WebsitePolicies::modalContainerObservationPolicy()` に依存する。

## Discussion
setter は `coreModalContainerObservationPolicy` で変換して設定する。getter は `modalContainerObservationPolicy` で逆変換する。

## References
- [`WKWebpagePreferencesPrivate.h#L115`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L115)
- [`WKWebpagePreferences.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L594)
- [`WKWebpagePreferences.mm#L594`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L594)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
