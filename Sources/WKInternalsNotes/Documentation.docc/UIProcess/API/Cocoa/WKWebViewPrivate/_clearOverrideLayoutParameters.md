# ``WKInternalsNotes/WKWebView/_clearOverrideLayoutParameters()``

`_clearOverrideLayoutParameters` をリセットする。

## Objective-C Declaration
```objective-c
- (void)_clearOverrideLayoutParameters WK_API_AVAILABLE(ios(11.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L760)
- [`WKWebViewIOS.mm#L4915`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4915)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
