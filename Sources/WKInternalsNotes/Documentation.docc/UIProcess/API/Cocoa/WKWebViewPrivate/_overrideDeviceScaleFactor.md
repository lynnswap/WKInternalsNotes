# ``WKInternalsNotes/WKWebView/_overrideDeviceScaleFactor``

`_overrideDeviceScaleFactor` の値を取得/設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setOverrideDeviceScaleFactor:) CGFloat _overrideDeviceScaleFactor WK_API_AVAILABLE(macos(10.11), ios(16.4));
```

## Discussion
getter/setter を通じて値を取得/設定する。 setter は `_setOverrideDeviceScaleFactor:`。

## References
- [`API/Cocoa/WKWebViewPrivate.h#L529`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L529)
- [`API/Cocoa/WKWebView.mm#L6251`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6251)
- [`API/Cocoa/WKWebView.mm#L6246`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebView.mm#L6246)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
