# ``WKInternalsNotes/WKWebView/_doAfterNextStablePresentationUpdate(_:)``

`_doAfterNextStablePresentationUpdate` を実行する。

## Objective-C Declaration
```objective-c
- (void)_doAfterNextStablePresentationUpdate:(dispatch_block_t)updateBlock WK_API_AVAILABLE(ios(10.3));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h#L732`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h#L732)
- [`WKWebViewIOS.mm#L4483`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4483)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
