# ``WKInternalsNotes/WKWebpagePreferences/_mouseEventPolicy``

マウスイベントのポリシーを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMouseEventPolicy:) _WKWebsiteMouseEventPolicy _mouseEventPolicy WK_API_AVAILABLE(macos(11.0), ios(14.0));
```

## Default Value
初期値は `WebsitePolicies::mouseEventPolicy()` に依存する。

## Discussion
setter は `coreMouseEventPolicy` で変換して設定する。getter は `mouseEventPolicy` で逆変換する。

## References
- [`WKWebpagePreferencesPrivate.h#L114`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h#L114)
- [`WKWebpagePreferences.mm#L579`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L579)
- [`WKWebpagePreferences.mm#L584`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences.mm#L584)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
