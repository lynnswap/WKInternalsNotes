# ``WKInternalsNotes/WKWebView/_minimumEffectiveDeviceWidth``

`_minimumEffectiveDeviceWidth` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setMinimumEffectiveDeviceWidth:) CGFloat _minimumEffectiveDeviceWidth WK_API_AVAILABLE(macos(10.14.4), ios(12.2));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setMinimumEffectiveDeviceWidth:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L294)
- [`API/Cocoa/WKWebView.mm#L6015`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6015)
- [`API/Cocoa/WKWebView.mm#L6001`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6001)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
