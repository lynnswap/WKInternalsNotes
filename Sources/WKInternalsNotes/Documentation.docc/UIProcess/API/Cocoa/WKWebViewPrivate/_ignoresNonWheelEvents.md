# ``WKInternalsNotes/WKWebView/_ignoresNonWheelEvents``

`_ignoresNonWheelEvents` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, readwrite, setter=_setIgnoresNonWheelEvents:) BOOL _ignoresNonWheelEvents WK_API_AVAILABLE(macos(10.13.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setIgnoresNonWheelEvents:`。

## References
- [`WKWebViewPrivate.h#L826`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L826)
- [`WKWebViewMac.mm#L1466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1466)
- [`WKWebViewMac.mm#L1466`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/mac/WKWebViewMac.mm#L1466)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
