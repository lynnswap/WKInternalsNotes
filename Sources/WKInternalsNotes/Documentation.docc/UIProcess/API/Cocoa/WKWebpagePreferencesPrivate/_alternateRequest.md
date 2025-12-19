# ``WKInternalsNotes/WKWebpagePreferences/_alternateRequest``

代替リクエストを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setAlternateRequest:) NSURLRequest *_alternateRequest WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA), visionos(WK_XROS_TBA));
```

## Default Value
初期値は `WebsitePolicies::alternateRequest()` の状態に依存する。

## Discussion
setter は `setAlternateRequest` を呼び、getter は `alternateRequest().nsURLRequest(UpdateHTTPBody)` を返す。

## References
- [`WKWebpagePreferencesPrivate.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L134)
- [`WKWebpagePreferences.mm#L810`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L810)
- [`WKWebpagePreferences.mm#L815`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L815)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
