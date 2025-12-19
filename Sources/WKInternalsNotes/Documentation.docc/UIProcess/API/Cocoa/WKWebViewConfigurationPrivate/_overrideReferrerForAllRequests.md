# ``WKInternalsNotes/WKWebViewConfiguration/_overrideReferrerForAllRequests``

すべてのリクエストの referrer を上書きする。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverrideReferrerForAllRequests:) NSString *_overrideReferrerForAllRequests WK_API_AVAILABLE(macos(WK_MAC_TBA), ios(WK_IOS_TBA));
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- この API を使わない場合: referrer は通常の決定ロジックに従う（`nil`）。
- `_overrideReferrerForAllRequests` を設定すると: WebPage 作成時の parameters に渡され、すべてのリクエストで上書きされる。
- `nil` に戻すと: 上書きを解除する。

## Details
- null 文字列は `nil` として返る

## References
- [`WKWebViewConfigurationPrivate.h#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L99)
- [`WKWebViewConfiguration.mm#L790`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L790)
- [`WKWebViewConfiguration.mm#L790`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L790)
- [`APIPageConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIPageConfiguration.h)
- [`WebPageProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/WebPageProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
