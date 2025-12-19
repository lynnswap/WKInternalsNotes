# ``WKInternalsNotes/WKWebView/_setEphemeralUIEventAttribution(_:forApplicationWithBundleID:)``

`_setEphemeralUIEventAttribution` を設定する。

## Objective-C Declaration
```objective-c
- (void)_setEphemeralUIEventAttribution:(UIEventAttribution *)attribution forApplicationWithBundleID:(NSString *)bundleID WK_API_AVAILABLE(ios(16.0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L672`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L672)
- [`WKWebViewIOS.mm#L4259`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4259)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
