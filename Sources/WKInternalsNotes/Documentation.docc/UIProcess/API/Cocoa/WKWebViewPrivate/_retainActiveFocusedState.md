# ``WKInternalsNotes/WKWebView/_retainActiveFocusedState()``

`_retainActiveFocusedState` を実行する。

## Objective-C Declaration
```objective-c
- (void (^)(void))_retainActiveFocusedState WK_API_AVAILABLE(ios(9_0));
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewPrivate.h)
- [`WKWebViewIOS.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
