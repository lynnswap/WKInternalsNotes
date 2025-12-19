# ``WKInternalsNotes/WKWebView/_willOpenAppLink()``

`_willOpenAppLink` を実行する。

## Objective-C Declaration
```objective-c
- (void)_willOpenAppLink WK_API_AVAILABLE(ios(14.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L786)
- [`WKWebViewIOS.mm#L5047`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L5047)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
